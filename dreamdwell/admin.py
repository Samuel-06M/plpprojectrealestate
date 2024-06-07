from django.contrib import admin
from .models import Client, DreamDwellProperty
from .models import Booking

# Register the models here

class DreamDwellPropertyAdmin(admin.ModelAdmin):
    list_display = ('category', 'address', 'price', 'bedrooms', 'bathrooms', 'area', 'floor', 'parking_spots', 'availability')
    search_fields = ('category', 'address')

    def availability(self, obj):
        if obj.booking:
            return "Booked"
        else:
            return "Available"
    availability.short_description = 'Availability'

# class ClientAdmin(admin.ModelAdmin):
#     list_display = ('name', 'email', 'phone', 'visit_date')
#     search_fields = ('name', 'email', 'phone', 'visit_date')

class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'visit_date')
    search_fields = ('name', 'email', 'phone', 'visit_date')

admin.site.register(DreamDwellProperty, DreamDwellPropertyAdmin)
# admin.site.register(Client)
admin.site.register(Booking, BookingAdmin)

