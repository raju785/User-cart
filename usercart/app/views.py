from django.db.models.query import QuerySet
from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import generics


class ItemList(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    
    serializer_class = ItemSerializer

class ItemListDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    
    serializer_class = ItemSerializer


class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    
    serializer_class = OrderSerializer

class OrderListDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    
    serializer_class = OrderSerializer

