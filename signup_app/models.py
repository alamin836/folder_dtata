from django.db import models

class signupdata(models.Model):
    UserName=models.CharField(max_length=100)
    MobileNo=models.IntegerField()
    Email=models.EmailField()
    Password=models.CharField(max_length=60)
