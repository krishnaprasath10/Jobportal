from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Postjob(models.Model):
    Email=models.EmailField(max_length=50)
    Job_Title=models.CharField(max_length=50)
    Location=models.CharField(max_length=50)
    Job_Region =models.CharField(max_length=50)
    Job_Type= models.CharField(max_length=50)
    Job_Description=models.CharField(max_length=50)
    Company_Name=models.CharField(max_length=50)
    Company_Description=models.CharField(max_length=50)
    Website=models.CharField(max_length=50)
    Facebook_Username =models.CharField(max_length=50)
    Twitter_Username =models.CharField(max_length=50)
    Linkedin_Username =models.CharField(max_length=50)
    
class Contacts(models.Model):
    First_name=models.EmailField(max_length=50)
    Last_name=models.CharField(max_length=50)
    Email=models.EmailField(max_length=50)
    Subject =models.CharField(max_length=50)
    Message= models.CharField(max_length=50)