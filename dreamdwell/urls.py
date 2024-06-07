from django.urls import path
from django.views.generic import TemplateView
from dreamdwell import views
from django.contrib import admin

urlpatterns = [
    path('', views.index, name='index'),  # Example URL pattern for the index page
    path('admin/', admin.site.urls),  # This line includes the admin URLs
    path('properties/', views.properties, name='properties'),  # Example URL pattern for the properties page
    path('property-details/<int:property_id>/', views.property_details, name='property_details'),  # Example URL pattern for property details page
    path('contact/', views.contact, name='contact'),  # Example URL pattern for the contact page
    path('booking.html', views.booking, name='booking'),  # To match 'booking.html'
    path('booking_success', views.booking_success, name='booking_success'),  # To match 'booking_success.html'
]
