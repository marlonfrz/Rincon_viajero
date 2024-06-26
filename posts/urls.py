from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [path('<slug:slug>', views.travel_detail, name='travel_detail')]
