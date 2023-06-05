# import serializers from the REST framework
from rest_framework import serializers
 

from django.contrib.auth.models import User

from rest_framework import serializers, validators
from .models import Product,Order,Cart



class storeSerializer(serializers.ModelSerializer):
 
    # create a meta class
    class Meta:
        model = Product
        fields = ('name', 'slug','price','quantity','description','image')

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model= Order
        fields =('user','product','quantity','ordered','ordered_date')


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model= Cart
        fields =('user','orders')
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'