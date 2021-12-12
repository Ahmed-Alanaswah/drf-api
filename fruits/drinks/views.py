from django.db.models.query import QuerySet
from django.shortcuts import render
from rest_framework import generics, serializers
# Create your views here.
from .serializers import DrinkSerializers
from .models import Drink

class DrinkList(generics.ListCreateAPIView):
    queryset=Drink.objects.all()
    serializer_class = DrinkSerializers



class DrinkDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Drink.objects.all()
    serializer_class = DrinkSerializers    