from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Meal
from .serializers import MealSerializer

# -------------------------------------------------------meal_list_view-----------------------------------------------------------------

@api_view(['GET'])
def meal_list_view(request):
    meals = Meal.objects.all()
    serializer = MealSerializer(meals, many=True)
    return Response(serializer.data)

# -------------------------------------------------------meal_detail_view-----------------------------------------------------------------

@api_view(['GET'])
def meal_detail_view(request):
    meal_pk = request.headers.get('pk')
    if not meal_pk:
        return Response(
            {"error": "PK header is required"}, status=status.HTTP_400_BAD_REQUEST
        )

    try:
        meal = Meal.objects.get(pk=meal_pk)
    except Meal.DoesNotExist:
        return Response(
            {"message": "Meal does not exist"}, status=status.HTTP_404_NOT_FOUND
        )

    serializer = MealSerializer(meal)
    return Response(serializer.data, status=status.HTTP_200_OK)

# -------------------------------------------------------meal_create_view-----------------------------------------------------------------

@api_view(['POST'])
def meal_create_view(request):
    serializer = MealSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# -------------------------------------------------------meal_update_view-----------------------------------------------------------------

@api_view(['PUT'])
def meal_update_view(request):
    meal_pk = request.headers.get('pk')
    if not meal_pk:
        return Response(
            {"error": "PK header is required"}, status=status.HTTP_400_BAD_REQUEST
        )

    try:
        meal = Meal.objects.get(pk=meal_pk)
    except Meal.DoesNotExist:
        return Response(
            {"message": "Meal does not exist"}, status=status.HTTP_404_NOT_FOUND
        )

    serializer = MealSerializer(meal, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# -------------------------------------------------------meal_partial_update_view-----------------------------------------------------------------

@api_view(['PATCH'])
def meal_partial_update_view(request):
    meal_pk = request.headers.get('pk')
    if not meal_pk:
        return Response(
            {"error": "PK header is required"}, status=status.HTTP_400_BAD_REQUEST
        )

    try:
        meal = Meal.objects.get(pk=meal_pk)
    except Meal.DoesNotExist:
        return Response(
            {"message": "Meal does not exist"}, status=status.HTTP_404_NOT_FOUND
        )

    serializer = MealSerializer(meal, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# -------------------------------------------------------meal_delete_view-----------------------------------------------------------------

@api_view(['DELETE'])
def meal_delete_view(request):
    meal_pk = request.headers.get('pk')
    if not meal_pk:
        return Response(
            {"error": "PK header is required"}, status=status.HTTP_400_BAD_REQUEST
        )

    try:
        meal = Meal.objects.get(pk=meal_pk)
    except Meal.DoesNotExist:
        return Response(
            {"message": "Meal does not exist"}, status=status.HTTP_404_NOT_FOUND
        )

    meal.delete()
    return Response(
        {"message": "Meal deleted successfully"}, status=status.HTTP_204_NO_CONTENT
    )
