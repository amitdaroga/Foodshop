from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# all user details in user table 
class All_User(models.Model):
    First_Name=models.CharField(max_length=100)
    Last_Name=models.CharField(max_length=100)
    Email=models.EmailField(max_length=100,unique=True)
    password=models.CharField(max_length=100)
# used for otp verification
class Verification(models.Model):
    Token=models.CharField(max_length=500)
    Token_id=models.CharField(max_length=500)

class ProductDetails(models.Model):
    Email_id=models.EmailField(max_length=100)
    ProductName=models.CharField(max_length=200)
    ProductCategory=models.CharField(max_length=200)
    ProductDueDate=models.DateField(max_length=100)