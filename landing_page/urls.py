from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('insights/', views.blog, name='insights'),
    path('contact/', views.contact, name='contact'),
    path('portfolio_new/', views.portfolio_new, name='portfolio_new'),
    path('careers/', views.careers, name='careers'),
    path('services/', views.services, name='services'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('what-we-do/', views.what_we_do, name='what_we_do'),
]