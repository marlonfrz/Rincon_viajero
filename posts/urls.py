from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.posts_list, name='posts_list'),
    path('<str:category>/<slug:travel_slug>/', views.post_detail, name='post_detail'),
    path('vuelos/', views.flights_list, name='flights_list'),
    path('vuelos-y-hotel/', views.flights_and_hotel_list, name='flights_and_hotel_list'),
    path('alojamiento/', views.accommodation_list, name='accommodation_list'),
    path('cruceros/', views.cruises_list, name='cruises_list'),
    path('politica-de-cookies/', views.cookies_policy, name='cookies_policy'),
    path('sobre-nosotros/', views.about_us, name='about_us'),
    path('avisos-legales/', views.legal_warning, name='legal_warning'),
    path('test/', views.test, name='test'),
    path('test2/', views.test2, name='test2'),
]
