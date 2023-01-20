from django.db import models

class UserAccount(models.Model):
    
    firstname= models.CharField(max_length=200)
    surname= models.CharField(max_length=200)
    username= models.CharField(max_length=300)
    email= models.EmailField()
    phone= models.CharField(max_length=12)