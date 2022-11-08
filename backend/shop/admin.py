from django.contrib import admin

from shop.models import (Store, 
                         Car, 
                         Customer)


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    ...


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    ...
    
    
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    ...
