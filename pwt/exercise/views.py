from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Exercise
from .serializers import ExerciseSerializer


# ----------------------------------------------------------exercise_list_view---------------------------------------------------------------
# List all exercises
@api_view(['GET'])
def exercise_list_view(request):
    exercises = Exercise.objects.all()
    serializer = ExerciseSerializer(exercises, many=True)
    return Response(serializer.data)



# ----------------------------------------------------------exercise_list_view---------------------------------------------------------------
# Retrieve a specific exercise by its primary key
@api_view(['GET'])
def exercise_detail_view(request):
    exercise_pk = request.headers.get('pk')
    if not exercise_pk:
        return Response(
            {"error": "PK header is required"}, status=status.HTTP_400_BAD_REQUEST
        )

    try:
        exercise = Exercise.objects.get(pk=exercise_pk)
    except Exercise.DoesNotExist:
        return Response(
            {"message": "Exercise does not exist"}, status=status.HTTP_404_NOT_FOUND
        )

    serializer = ExerciseSerializer(exercise)
    return Response(serializer.data, status=status.HTTP_200_OK)



# ----------------------------------------------------------exercise_list_view---------------------------------------------------------------
# Create a new exercise
@api_view(['POST'])
def exercise_create_view(request):
    serializer = ExerciseSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




# ----------------------------------------------------------exercise_list_view---------------------------------------------------------------
# Partially update an existing exercise
@api_view(['PATCH'])
def exercise_partial_update_view(request):
    exercise_pk = request.headers.get('pk')
    if not exercise_pk:
        return Response(
            {"error": "PK header is required"}, status=status.HTTP_400_BAD_REQUEST
        )

    try:
        exercise = Exercise.objects.get(pk=exercise_pk)
    except Exercise.DoesNotExist:
        return Response(
            {"message": "Exercise does not exist"}, status=status.HTTP_404_NOT_FOUND
        )

    serializer = ExerciseSerializer(exercise, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(
            {"message": "Exercise partially updated successfully", "data": serializer.data},
            status=status.HTTP_200_OK
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




# ----------------------------------------------------------exercise_list_view---------------------------------------------------------------
# Delete an exercise
@api_view(['DELETE'])
def exercise_delete_view(request):
    exercise_pk = request.headers.get('pk')
    if not exercise_pk:
        return Response(
            {"error": "PK header is required"}, status=status.HTTP_400_BAD_REQUEST
        )

    try:
        exercise = Exercise.objects.get(pk=exercise_pk)
    except Exercise.DoesNotExist:
        return Response(
            {"message": "Exercise does not exist"}, status=status.HTTP_404_NOT_FOUND
        )

    exercise.delete()
    return Response(
        {"message": "Exercise deleted successfully"}, status=status.HTTP_204_NO_CONTENT
    )
