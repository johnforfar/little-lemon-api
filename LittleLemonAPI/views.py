# ./LittleLemonAPI/views.py

from django.shortcuts import render
from rest_framework import generics
from .models import Category, MenuItem
from .serializers import CategorySerializer, MenuItemSerializer

class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class MenuItemListCreateView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class MenuItemRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
