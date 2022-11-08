from django.db import models
from django.utils import timezone


class Base(models.Model):
    created = models.DateTimeField(auto_now_add=timezone.now)
    updated = models.DateTimeField(auto_now=timezone.now)
    active = models.BooleanField(default=True)
    
    class Meta:
        abstract = True
        
        
class Car(Base):

    class Color(models.TextChoices):
        BLUE = 'B', 'Blue'
        GREY = 'G', 'Grey'
        YELLOW = 'Y', 'Yellow'
        
    class CarModel(models.TextChoices):
        CONVERTIBLE = 'CVTB', 'Convertible'
        HATCH = 'HT', 'Hatch'
        SEDAN = 'SD', 'Sedan'
        
    name = models.CharField(max_length=10)
    color = models.CharField(max_length=1, choices=Color.choices)
    model = models.CharField(max_length=4, choices=CarModel.choices)

    class Meta:
        ordering = ['-name']
        
        
class Customer(Base):
    name = models.CharField(max_length=150)
    
    class Meta:
        ordering = ['-name']
        
        
class Store(Base):
    name = models.CharField(max_length=150)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='shop_stores')
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='shop_stores')
    
    
class Order(Base):
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='shop_orders')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    
    class Meta:
        ordering = ['-created']
