from django.shortcuts import render, redirect
from django . contrib import messages
from .models import Booking, Client


def index(request):
   users=Client.object.all()
   bookings=Booking.object.all()
   
   return render(request, 'dreamdwell/index.html',{"users":users,"bookings":bookings})

def properties(request):
    """Render the properties page."""
    return render(request, 'dreamdwell/properties.html')

def property_details(request):
    """Render the property details page."""
    return render(request, 'dreamdwell/property-details.html')

def contact(request):
    """Render the contact page."""
    return render(request, 'dreamdwell/contact.html')

def booking(request):
    """Handle booking form submission."""
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        visit_date = request.POST.get('visit_date')
        
        if name and email and phone and visit_date:  # Check if all fields are filled
            # Create a new Booking object and save it to the database
            booking = Booking.objects.create(name=name, email=email, phone=phone, visit_date=visit_date)
            
            if booking:
                messages.success(request, 'Booking successful!')
            else:
                messages.error(request, 'Failed to process booking. Please try again.')
        else:
            messages.error(request, 'Please fill in all fields.')
            
        return redirect('properties')  # Redirect after processing form submission
    return render(request, 'dreamdwell/booking.html')


def booking_success(request):
    return render(request, 'dreamdwell/booking_success.html')

