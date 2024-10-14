from rest_framework import serializers
from .models import ExerciseLibrary

class ExerciseLibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = ExerciseLibrary
        fields = '__all__'
