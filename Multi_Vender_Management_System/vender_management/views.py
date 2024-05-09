from django.shortcuts import render
from vender_management.models import vendor ,purchase_order
from vender_management.serializers import vendorSerializer ,POSerialixer
from rest_framework import viewsets
from rest_framework.decorators import action
# Create your views here.


class venderAPIViews(viewsets.ModelViewSet):
    queryset=vendor.objects.all()
    serializer_class=vendorSerializer

class POAPI(viewsets.ModelViewSet):
    queryset=purchase_order.objects.all()
    serializer_class=POSerialixer