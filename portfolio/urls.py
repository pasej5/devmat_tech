from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.index, name='index'),
    path('service/web-development/', views.web_dev_service_page, name='web_dev_service_page'),
]
