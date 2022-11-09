from django.contrib import admin

from shop.models import (Store, 
                         Car, 
                         Customer,
                         Order)


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    ...


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    ...
    
    
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    ...


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    ...
