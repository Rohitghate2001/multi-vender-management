from rest_framework import serializers
from vender_management.models import vendor,purchase_order


class vendorSerializer(serializers.ModelSerializer):
    class Meta:
        model=vendor
        fields=['name','contact_details','address']

class POSerialixer(serializers.ModelSerializer):
    po_number=serializers.ReadOnlyField()
    class Meta:
        model=purchase_order
        fields='__all__'

# class historical_performance_seializer(serializers.ModelSerializer):
#     class Meta:
    
#         model=Historical_Performance
#         fields="__all__"
