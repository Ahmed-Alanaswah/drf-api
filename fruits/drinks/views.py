from django.db.models.query import QuerySet
from django.shortcuts import render
from rest_framework import generics, permissions, serializers
# Create your views here.
from .serializers import DrinkSerializers
from .models import Drink
from .permissions import IsAuthentecatedOrReadOnly
class DrinkList(generics.ListCreateAPIView):
    queryset=Drink.objects.all()
    serializer_class = DrinkSerializers
    permission_class = (IsAuthentecatedOrReadOnly,)

class DrinkDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Drink.objects.all()
    serializer_class = DrinkSerializers    
    permission_class = (IsAuthentecatedOrReadOnly,)



