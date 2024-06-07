# Create your models here.
from django.db import models



class Client(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Booking(models.Model):
    name = models.CharField(max_length=100, default='Name')
    email = models.EmailField(default='email@example.com')
    phone = models.CharField(max_length=15, default='0000000000')
    visit_date = models.DateField(default='2024-01-01')

    def __str__(self):
        return self.name

    def __str__(self):
        return str(self.visit_date)

class DreamDwellProperty(models.Model):
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE, null=True, blank=True)
    category_choices = [
        ('Villa', 'Villa'),
        ('Apartment', 'Apartment'),
        ('Penthouse', 'Penthouse'),
        ('Condo', 'Condo'),
    ]
    
    category = models.CharField(max_length=20, choices=category_choices)
    address = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    area = models.DecimalField(max_digits=10, decimal_places=2)
    floor = models.IntegerField()
    parking_spots = models.IntegerField()
    image = models.ImageField(upload_to='dreamdwell_property_images/')
    description = models.TextField()

    def __str__(self):
        return f"{self.category} - {self.address}"

    
