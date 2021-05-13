from django.shortcuts import render
from home.models import Booking
from django.contrib import messages

# Create your views here.
def booking(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        destination=request.POST['destination']
        checkin=request.POST['checkin']
        checkout=request.POST['checkout']
        adults=request.POST['adults']
        children=request.POST['children']
        queries =request.POST['queries']
        if len(name)<2 or len(email)<3 or len(phone)<10 or len(queries)<4:
            messages.error(request, "Please fill the form correctly")
        else:
            booking=Booking(name=name, email=email, phone=phone, destination=destination, checkin=checkin, checkout=checkout, adults=adults, children=children, queries=queries)
            booking.save()
            messages.success(request, "Your message has been successfully sent")
    return render(request, "booking.html")