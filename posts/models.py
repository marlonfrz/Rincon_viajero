from django.db import models
from django.urls import reverse


class TravelPost(models.Model):

    class Status(models.TextChoices):
        ACTIVE = "AC", "Active"
        DISABLED = "DS", "Disable"
        CANCELLED = "CN", "Cancelled"

    travel_name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    cupon = models.CharField(max_length=20, blank=True, null=True)
    slug = models.SlugField()
    url = models.URLField()
    description = models.CharField(max_length=1000)
    photo = models.ImageField(upload_to='travels/%Y/%m/%d/', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default=Status.ACTIVE, choices=Status.choices)

    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['-created']),
        ]

    def __str__(self):
        return self.travel_name

    def get_absolute_url(self):
        return reverse("post_detail", args=[self.id])
