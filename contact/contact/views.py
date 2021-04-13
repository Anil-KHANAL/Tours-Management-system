from django.shorcuts import render
from contact.models import ContactUs
from django.contrib import messsages

def Insertrecord(request):
    if request.method=='POST':
        if request.POST.get('Name') and request.POST.get('Email') and request.POST.get('Messages'):
            client=ContactUs
            client.Name=request.POST.get('Name')
            client.Email=request.POST.get('Email')
            client.Messages=request.POST.get('Messages')
            client.save()
            messsages.success(request, 'Thankyou for your choosing us!')
            return render(request, 'contact us.html')
        else:
            return render(request, 'contact us.html')