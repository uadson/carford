from rest_framework import serializers

from shop.models import Store, Car, Customer, Order


class CarSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Car
        fields = ('id', 'name', 'color', 'model')
        
        
class CustomerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Customer
        fields = ('id', 'name', 'store_id', 'created')
        
        
class OrderSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Order
        store = serializers.CharField(source = 'store.name')
        
    def get_fields(self):
        car = CarSerializer(many=True)
        id = serializers.IntegerField()
        store = serializers.CharField(source = 'store.name')
        customer = serializers.CharField(source = 'customer.name')
        created = serializers.DateTimeField()
        
        context = {
            'id': id,
            'name': store,
            'customer': customer,
            'car': car,
            'created': created
        }
        return context
        

class StoreSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Store
        fields = ('id', 'name')
