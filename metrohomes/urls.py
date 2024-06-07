"""
URL configuration for metrohomes project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from dreamdwell import views  # Importing views from the dreamdwell app
from django.views.generic import TemplateView
from django.contrib import admin

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),  # This line includes the admin URLs
    path('properties/', views.properties, name='properties'),
    path('property-details/', views.property_details, name='property_details'),
    path('contact/', views.contact, name='contact'),path('property-details/', views.property_details, name='property_details'),
    path('booking.html', views.booking, name='booking'),  # To match 'booking.html'
    path('booking_success', views.booking_success, name='booking_success'),  # To match 'booking_success.html'
]

