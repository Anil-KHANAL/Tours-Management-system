from django.shortcuts import render
from home.models import Booking
from django.contrib import messages

# Create your views here.
def booking(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        content =request.POST['content']
        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<4:
            messages.error(request, "Please fill the form correctly")
        else:
            booking=Booking(name=name, email=email, phone=phone, content=content)
            booking.save()
            messages.success(request, "Your message has been successfully sent")
    return render(request, "booking.html")