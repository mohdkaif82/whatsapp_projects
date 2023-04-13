from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('whatsapp/', views.WhatsAppView.as_view(), name='whatsapp'),
    path('facebook/', views.WhatsAppSms.as_view(), name='facebook'),
]