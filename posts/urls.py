from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.posts_list, name='posts_list'),
    path('post/<slug:travel_slug>/', views.post_detail, name='post_detail'),
]
