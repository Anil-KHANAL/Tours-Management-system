from django.shortcuts import render
from contact.models import ContactUs
from django.contrib import messages 

def Insertrecord(request):
    if request.method=='POST':
        if request.POST.get('Name') and request.POST.get('Email') and request.POST.get('Messages'):
            client=ContactUs()
            client.Name=request.POST.get('Name')
            client.Email=request.POST.get('Email')
            client.Messages=request.POST.get('Messages')
            client.save()
            messages.success(request, 'Thankyou for choosing us!')
            return render(request,'contact_us.html')
    else:
        return render(request,'contact_us.html')