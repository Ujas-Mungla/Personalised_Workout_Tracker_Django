from django.shortcuts import render

# Create your views here.

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Goal
from .serializers import GoalSerializer



# -------------------------------------------------------goal_list_view-----------------------------------------------------------------

@api_view(['GET'])
def goal_list_view(request):
    goals = Goal.objects.all()
    serializer = GoalSerializer(goals, many=True)
    return Response(serializer.data)




# -------------------------------------------------------goal_detail_view-----------------------------------------------------------------


@api_view(['GET'])
def goal_detail_view(request):
    goal_pk = request.headers.get('pk')
    if not goal_pk:
        return Response(
            {"error": "PK header is required"}, status=status.HTTP_400_BAD_REQUEST
        )

    try:
        goal = Goal.objects.get(pk=goal_pk)
    except Goal.DoesNotExist:
        return Response(
            {"message": "Goal does not exist"}, status=status.HTTP_404_NOT_FOUND
        )

    serializer = GoalSerializer(goal)
    return Response(serializer.data, status=status.HTTP_200_OK)





# -------------------------------------------------------goal_create_view-----------------------------------------------------------------


@api_view(['POST'])
def goal_create_view(request):
    serializer = GoalSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





# -------------------------------------------------------goal_update_view-----------------------------------------------------------------


@api_view(['PUT'])
def goal_update_view(request):
    goal_pk = request.headers.get('pk')
    if not goal_pk:
        return Response(
            {"error": "PK header is required"}, status=status.HTTP_400_BAD_REQUEST
        )

    try:
        goal = Goal.objects.get(pk=goal_pk)
    except Goal.DoesNotExist:
        return Response(
            {"message": "Goal does not exist"}, status=status.HTTP_404_NOT_FOUND
        )

    serializer = GoalSerializer(goal, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# -------------------------------------------------------goal_partial_update_view-----------------------------------------------------------------


@api_view(['PATCH'])
def goal_partial_update_view(request):
    goal_pk = request.headers.get('pk')
    if not goal_pk:
        return Response(
            {"error": "PK header is required"}, status=status.HTTP_400_BAD_REQUEST
        )

    try:
        goal = Goal.objects.get(pk=goal_pk)
    except Goal.DoesNotExist:
        return Response(
            {"message": "Goal does not exist"}, status=status.HTTP_404_NOT_FOUND
        )

    serializer = GoalSerializer(goal, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# -------------------------------------------------------goal_delete_view-----------------------------------------------------------------



@api_view(['DELETE'])
def goal_delete_view(request):
    goal_pk = request.headers.get('pk')
    if not goal_pk:
        return Response(
            {"error": "PK header is required"}, status=status.HTTP_400_BAD_REQUEST
        )

    try:
        goal = Goal.objects.get(pk=goal_pk)
    except Goal.DoesNotExist:
        return Response(
            {"message": "Goal does not exist"}, status=status.HTTP_404_NOT_FOUND
        )

    goal.delete()
    return Response(
        {"message": "Goal deleted successfully"}, status=status.HTTP_204_NO_CONTENT
    )
