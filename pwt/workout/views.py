from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Workout
from .serializers import WorkoutSerializer

# -------------------------------------------------------workout_list_view------------------------------------------------------------

@api_view(['GET'])
def workout_list_view(request):
    workouts = Workout.objects.all()
    serializer = WorkoutSerializer(workouts, many=True)
    return Response(serializer.data)


# -------------------------------------------------------workout_detail_view------------------------------------------------------------


@api_view(['GET'])
def workout_detail_view(request):
    workout_pk = request.headers.get('pk')
    if not workout_pk:
        return Response(
            {"error": "PK header is required"}, status=status.HTTP_400_BAD_REQUEST
        )

    try:
        workout = Workout.objects.get(pk=workout_pk)
    except Workout.DoesNotExist:
        return Response(
            {"message": "Workout does not exist"}, status=status.HTTP_404_NOT_FOUND
        )

    serializer = WorkoutSerializer(workout)
    return Response(serializer.data, status=status.HTTP_200_OK)


# -------------------------------------------------------workout_create_view------------------------------------------------------------



@api_view(['POST'])
def workout_create_view(request):
    serializer = WorkoutSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# -------------------------------------------------------workout_partial_update_view------------------------------------------------------------




@api_view(['PATCH'])
def workout_partial_update_view(request):
    workout_pk = request.headers.get('pk')
    if not workout_pk:
        return Response(
            {"error": "PK header is required"}, status=status.HTTP_400_BAD_REQUEST
        )

    try:
        workout = Workout.objects.get(pk=workout_pk)
    except Workout.DoesNotExist:
        return Response(
            {"message": "Workout does not exist"}, status=status.HTTP_404_NOT_FOUND
        )

    serializer = WorkoutSerializer(workout, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(
            {"message": "Workout partially updated successfully", "data": serializer.data},
            status=status.HTTP_200_OK
        )
    return Response(
        serializer.errors, status=status.HTTP_400_BAD_REQUEST
    )



# -------------------------------------------------------workout_delete_view------------------------------------------------------------

@api_view(['DELETE'])
def workout_delete_view(request):
    workout_pk = request.headers.get('pk')
    if not workout_pk:
        return Response(
            {"error": "PK header is required"}, status=status.HTTP_400_BAD_REQUEST
        )

    try:
        workout = Workout.objects.get(pk=workout_pk)
    except Workout.DoesNotExist:
        return Response(
            {"message": "Workout does not exist"}, status=status.HTTP_404_NOT_FOUND
        )

    workout.delete()
    return Response(
        {"message": "Workout deleted successfully"}, status=status.HTTP_204_NO_CONTENT
    )