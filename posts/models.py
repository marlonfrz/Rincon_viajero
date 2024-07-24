from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify


class TravelPost(models.Model):

    class Status(models.TextChoices):
        ACTIVE = "AC", "Active"
        DISABLED = "DS", "Disable"
        CANCELLED = "CN", "Cancelled"

    travel_name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    coupon = models.CharField(max_length=20, blank=True, null=True)
    slug = models.SlugField(unique=True)
    url = models.URLField()
    description = models.CharField(max_length=2500)
    detail_description = models.CharField(max_length=400)
    photo = models.ImageField(upload_to='travels/%Y/%m/%d/', blank=False, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    deadline = models.DateTimeField(null=True, blank=False)
    status = models.CharField(max_length=20, default=Status.ACTIVE, choices=Status.choices)

    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['-created']),
        ]

    def __str__(self):
        return self.travel_name

    def get_absolute_url(self):
        return reverse("posts:post_detail", args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.get_unique_slug()
        self.updated = timezone.now()
        super().save(*args, **kwargs)

    def get_unique_slug(self):
        slug = slugify(self.travel_name)
        unique_slug = slug
        counter = 1
        while TravelPost.objects.filter(slug=unique_slug).exists():
            unique_slug = f"{slug}-{counter}"
            counter += 1
        return unique_slug
