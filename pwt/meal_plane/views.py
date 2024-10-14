from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import MealPlan
from .serislizers import MealPlanSerializer

# -------------------------------------------------------mealplan_list_view-----------------------------------------------------------------

@api_view(['GET'])
def mealplan_list_view(request):
    mealplans = MealPlan.objects.all()
    serializer = MealPlanSerializer(mealplans, many=True)
    return Response(serializer.data)

# -------------------------------------------------------mealplan_detail_view-----------------------------------------------------------------

@api_view(['GET'])
def mealplan_detail_view(request):
    mealplan_pk = request.headers.get('pk')
    if not mealplan_pk:
        return Response(
            {"error": "PK header is required"}, status=status.HTTP_400_BAD_REQUEST
        )

    try:
        mealplan = MealPlan.objects.get(pk=mealplan_pk)
    except MealPlan.DoesNotExist:
        return Response(
            {"message": "MealPlan does not exist"}, status=status.HTTP_404_NOT_FOUND
        )

    serializer = MealPlanSerializer(mealplan)
    return Response(serializer.data, status=status.HTTP_200_OK)

# -------------------------------------------------------mealplan_create_view-----------------------------------------------------------------

@api_view(['POST'])
def mealplan_create_view(request):
    serializer = MealPlanSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# -------------------------------------------------------mealplan_update_view-----------------------------------------------------------------

@api_view(['PUT'])
def mealplan_update_view(request):
    mealplan_pk = request.headers.get('pk')
    if not mealplan_pk:
        return Response(
            {"error": "PK header is required"}, status=status.HTTP_400_BAD_REQUEST
        )

    try:
        mealplan = MealPlan.objects.get(pk=mealplan_pk)
    except MealPlan.DoesNotExist:
        return Response(
            {"message": "MealPlan does not exist"}, status=status.HTTP_404_NOT_FOUND
        )

    serializer = MealPlanSerializer(mealplan, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# -------------------------------------------------------mealplan_partial_update_view-----------------------------------------------------------------

@api_view(['PATCH'])
def mealplan_partial_update_view(request):
    mealplan_pk = request.headers.get('pk')
    if not mealplan_pk:
        return Response(
            {"error": "PK header is required"}, status=status.HTTP_400_BAD_REQUEST
        )

    try:
        mealplan = MealPlan.objects.get(pk=mealplan_pk)
    except MealPlan.DoesNotExist:
        return Response(
            {"message": "MealPlan does not exist"}, status=status.HTTP_404_NOT_FOUND
        )

    serializer = MealPlanSerializer(mealplan, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# -------------------------------------------------------mealplan_delete_view-----------------------------------------------------------------

@api_view(['DELETE'])
def mealplan_delete_view(request):
    mealplan_pk = request.headers.get('pk')
    if not mealplan_pk:
        return Response(
            {"error": "PK header is required"}, status=status.HTTP_400_BAD_REQUEST
        )

    try:
        mealplan = MealPlan.objects.get(pk=mealplan_pk)
    except MealPlan.DoesNotExist:
        return Response(
            {"message": "MealPlan does not exist"}, status=status.HTTP_404_NOT_FOUND
        )

    mealplan.delete()
    return Response(
        {"message": "MealPlan deleted successfully"}, status=status.HTTP_204_NO_CONTENT
    )
