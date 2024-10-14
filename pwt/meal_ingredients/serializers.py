from rest_framework import serializers
from .models import MealIngredient

class MealIngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = MealIngredient
        fields = '__all__'
