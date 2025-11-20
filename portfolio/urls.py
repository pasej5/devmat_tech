from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.index, name='index'),
    path('service/web-development/', views.web_dev_service_page, name='web_dev_service_page'),
    path('service/ai-machine-learning/', views.ai_ml_service_page, name='ai_ml_service_page'),
    path('service/api-development/', views.api_dev_service_page, name='api_dev_service_page'),
    path('service/cloud-computing/', views.cloud_service_page, name='cloud_service_page'),
]
