from django.db.models import fields
from rest_framework import serializers

from .models import Drink 

class DrinkSerializers(serializers.ModelSerializer):
    class Meta :
        fields=['title','author','updated','timestamp','content','published']
        model=Drink