from rest_framework import serializers

from shop.models import Store, Car, Customer, Order


class CarSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Car
        fields = ('id', 'name', 'color', 'model', 'created')
        
        
class CustomerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Customer
        fields = ('id', 'name', 'store_id', 'created')
        
        
class OrderSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Order
        fields = ('id', 'store_id', 'customer_id', 'car_id', 'created')
        

class StoreSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Store
        fields = ('id', 'name')
