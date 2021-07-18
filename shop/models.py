from django.db import models
 

# Create your models here.


class Contact(models.Model):
    name= models.CharField(max_length=30)
    email= models.EmailField(max_length=30)
    phone= models.CharField(max_length=30)
    desc= models.CharField(max_length=3000)
    def __str__(self):
        return self.name


class Customer(models.Model):
    username= models.CharField(max_length=30)
    email= models.EmailField(max_length=30)
    phone= models.CharField(max_length=30)
    password= models.CharField(max_length=3000)
    def __str__(self):
        return self.username


class Category(models.Model):
    name= models.CharField(max_length=30)
     
    def __str__(self):
        return self.name




class Product(models.Model):
    title= models.CharField(max_length=30)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price= models.IntegerField(default=500)
    
    desc= models.CharField(max_length=3000)
    img = models.ImageField(upload_to="images",default="")
    def __str__(self):
        return self.title        


class Order(models.Model):
    product  = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)   
    status = models.BooleanField(default=False) 
    price= models.IntegerField(default=500)   
    address=models.CharField(max_length=300)
    phone = models.CharField(max_length=30)
    quantity = models.IntegerField(max_length=300)
     
    def __str__(self):
        return self.address       


