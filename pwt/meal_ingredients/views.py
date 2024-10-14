from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import MealIngredient
from .serializers import MealIngredientSerializer



# -------------------------------------------------------------meal_ingredient_list_view-------------------------------------------------------

@api_view(['GET'])
def meal_ingredient_list_view(request):
    ingredients = MealIngredient.objects.all()
    serializer = MealIngredientSerializer(ingredients, many=True)
    return Response(serializer.data)



# -------------------------------------------------------------meal_ingredient_detail_view-------------------------------------------------------

@api_view(['GET'])
def meal_ingredient_detail_view(request):
    ingredient_pk = request.headers.get('pk')
    if not ingredient_pk:
        return Response({"error": "PK header is required"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        ingredient = MealIngredient.objects.get(pk=ingredient_pk)
    except MealIngredient.DoesNotExist:
        return Response({"message": "Meal Ingredient does not exist"}, status=status.HTTP_404_NOT_FOUND)

    serializer = MealIngredientSerializer(ingredient)
    return Response(serializer.data, status=status.HTTP_200_OK)



# -------------------------------------------------------------meal_ingredient_create_view-------------------------------------------------------


@api_view(['POST'])
def meal_ingredient_create_view(request):
    serializer = MealIngredientSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# -------------------------------------------------------------meal_ingredient_update_view-------------------------------------------------------


@api_view(['PUT'])
def meal_ingredient_update_view(request):
    ingredient_pk = request.headers.get('pk')
    if not ingredient_pk:
        return Response({"error": "PK header is required"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        ingredient = MealIngredient.objects.get(pk=ingredient_pk)
    except MealIngredient.DoesNotExist:
        return Response({"message": "Meal Ingredient does not exist"}, status=status.HTTP_404_NOT_FOUND)

    serializer = MealIngredientSerializer(ingredient, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# -------------------------------------------------------------meal_ingredient_partial_update_view-------------------------------------------------------


@api_view(['PATCH'])
def meal_ingredient_partial_update_view(request):
    ingredient_pk = request.headers.get('pk')
    if not ingredient_pk:
        return Response({"error": "PK header is required"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        ingredient = MealIngredient.objects.get(pk=ingredient_pk)
    except MealIngredient.DoesNotExist:
        return Response({"message": "Meal Ingredient does not exist"}, status=status.HTTP_404_NOT_FOUND)

    serializer = MealIngredientSerializer(ingredient, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# -------------------------------------------------------------meal_ingredient_delete_view-------------------------------------------------------


@api_view(['DELETE'])
def meal_ingredient_delete_view(request):
    ingredient_pk = request.headers.get('pk')
    if not ingredient_pk:
        return Response({"error": "PK header is required"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        ingredient = MealIngredient.objects.get(pk=ingredient_pk)
    except MealIngredient.DoesNotExist:
        return Response({"message": "Meal Ingredient does not exist"}, status=status.HTTP_404_NOT_FOUND)

    ingredient.delete()
    return Response({"message": "Meal Ingredient deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


