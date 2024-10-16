from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.posts_list, name='posts_list'),
    path('politica-de-cookies/', views.cookies_policy, name='cookies_policy'),
    path('sobre-nosotros/', views.about_us, name='about_us'),
    path('avisos-legales/', views.legal_warning, name='legal_warning'),
    path('test/', views.test, name='test'),
    path('test2/', views.test2, name='test2'),
    path('categoria/<str:category>/<slug:post_slug>/', views.post_detail, name='post_detail'),
    path('categoria/<str:category>/', views.posts_list, name='category_list'),
]
