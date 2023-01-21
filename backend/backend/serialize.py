from django.db.models import fields
from rest_framework import serializers
from backend.models import ProductModel,CustomerModel,OrdersModel,CartModel

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProductModel
        fields="__all__"
        
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomerModel
        fields="__all__"

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model=CartModel
        fields="__all__"

class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model=OrdersModel
        fields="__all__"