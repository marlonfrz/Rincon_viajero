import os

from django.db.models.signals import pre_delete
from django.dispatch import receiver

from .models import TravelPost


@receiver(pre_delete, sender=TravelPost)
def delete_travelpost_image(sender, instance, **kwargs):
    if instance.photo:
        if os.path.isfile(instance.photo.path):
            os.remove(instance.photo.path)
