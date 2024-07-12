from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.posts_list, name='posts_list'),
    path(
        'post_detail/<slug:slug>',
        views.post_detail,
        name="post_detail",
    ),
]
