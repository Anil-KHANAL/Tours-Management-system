from django.db import models


# Create your models here.
class Booking(models.Model):
     sno= models.AutoField(primary_key=True)
     name= models.CharField(max_length=100)
     phone= models.CharField(max_length=15)
     email= models.CharField(max_length=100)
     destination= models.CharField(max_length=100, blank=True)
     checkin = models.DateTimeField(help_text="Check In", null=True, blank=True)
     checkout = models.DateTimeField(blank=True, help_text="Check Out", null=True)
     adults= models.IntegerField(blank=True, null=True)
     children= models.IntegerField(blank=True, null=True)
     queries= models.TextField()
     timeStamp=models.DateTimeField(auto_now_add=True, blank=True)

     def __str__(self):
          return "Message from " + self.name + ' - ' + self.email