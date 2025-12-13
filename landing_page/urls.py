from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('insights/', views.blog, name='insights'),
    path('contact/', views.contact, name='contact'),
    path('portfolio_home/', views.portfolio, name='portfolio_home'),
    path('careers/', views.careers, name='careers'),
    path('services/', views.services, name='services'),
    path('about/', views.about, name='about'),
]