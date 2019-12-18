from rest_framework import serializer
from .models import Floreria

class FloreriaSerializer(serializers.ModelSerializer):

    class Meta:
        model = floreria
        fields= ['nombre','precio','descripcion']