from django.db import models

# Create your models here.


class Brewbella(models.Model):
    name=models.CharField(max_length=100,blank=True)
    price=models.IntegerField()
    quantity=models.IntegerField()   


class Cart(models.Model):
    productid=models.IntegerField()
    user=models.CharField(max_length=100,blank=True)
    productname=models.CharField(max_length=100,blank=True)
    proprice=models.IntegerField(blank=True)
    productquantity=models.IntegerField(blank=True)
    total=models.IntegerField(blank=True)
    



class Orders(models.Model):
    ordername=models.CharField(max_length=100)
    phoneno=models.IntegerField()
    address=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    pincode=models.IntegerField()
    email=models.EmailField(max_length=100)
    tamount=models.IntegerField()
    razorpay_order_id=models.CharField(max_length=100)
    ispaid=models.BooleanField(default=False)
    razorpay_payment_id=models.CharField(max_length=100)
    
    


 
