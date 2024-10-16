from django.contrib import admin

from .forms import TravelPostForm
from .models import TravelPost


@admin.register(TravelPost)
class PostAdmin(admin.ModelAdmin):
    form = TravelPostForm
    list_display = [
        'travel_name',
        'price',
        'coupon',
        'url',
        'description',
        'detail_description',
        'photo',
        'deadline',
        'status',
        'category',
    ]
    exclude = ('slug',)
