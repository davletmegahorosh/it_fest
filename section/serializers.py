from rest_framework import serializers
from .models import Sections


class SectionsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sections
        fields = ['id', 'name', 'icon']


class SectionsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sections
        fields = '__all__'
