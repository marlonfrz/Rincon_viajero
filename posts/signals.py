import io
import os

from django.core.files.base import ContentFile
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from PIL import Image

from .models import TravelPost


@receiver(pre_delete, sender=TravelPost)
def delete_travelpost_image(sender, instance, **kwargs):
    if instance.photo:
        if os.path.isfile(instance.photo.path):
            os.remove(instance.photo.path)


@receiver(post_save, sender=TravelPost)
def delete_cancelled_post(sender, instance, **kwargs):
    if instance.status == TravelPost.Status.CANCELLED:
        instance.delete()


@receiver(post_save, sender=TravelPost)
def convert_image_to_webp(sender, instance, **kwargs):
    if instance.photo and not instance.photo.name.endswith('.webp'):
        image = Image.open(instance.photo)

        buffer = io.BytesIO()
        image.save(buffer, format='WEBP')
        webp_image = ContentFile(
            buffer.getvalue(), name=instance.photo.name.replace('.jpg', '.webp')
        )

        instance.photo.save(instance.photo.name.replace('.jpg', '.webp'), webp_image, save=False)
        instance.save()
