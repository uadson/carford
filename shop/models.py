from django.db import models
from django.utils import timezone


class Base(models.Model):
    created = models.DateTimeField(auto_now_add=timezone.now)
    updated = models.DateTimeField(auto_now=timezone.now)
    active = models.BooleanField(default=True)
    
    class Meta:
        abstract = True
        

class Store(Base):
    name = models.CharField(max_length=150)
    
    class Meta:
        ordering = ['-name']
        

class Car(Base):

    class Color(models.TextChoices):
        BLUE = 'Blue', 'Blue'
        GREY = 'Grey', 'Grey'
        YELLOW = 'Yellow', 'Yellow'
        
    class CarModel(models.TextChoices):
        CONVERTIBLE = 'Convertible', 'Convertible'
        HATCH = 'Hatch', 'Hatch'
        SEDAN = 'Sedan', 'Sedan'
        
    name = models.CharField(max_length=10)
    color = models.CharField(max_length=6, choices=Color.choices)
    model = models.CharField(max_length=11, choices=CarModel.choices)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-name']
        
        
class Customer(Base):
    name = models.CharField(max_length=150)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    
    class Meta:
        ordering = ['-name']
  
    
class Order(Base):
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='shop_orders')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    
    class Meta:
        ordering = ['-created']
