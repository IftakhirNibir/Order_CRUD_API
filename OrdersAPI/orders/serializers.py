from rest_framework import serializers
from .models import Order_Detail

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order_Detail
        fields = ['user_id','product_id','quantity','payment_information']