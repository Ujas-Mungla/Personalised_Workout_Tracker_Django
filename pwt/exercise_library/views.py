from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import ExerciseLibrary
from .serializers import ExerciseLibrarySerializer

# -------------------------------------------------------exercise_library_list_view------------------------------------------------------------

@api_view(['GET'])
def exercise_library_list_view(request):
    exercises = ExerciseLibrary.objects.all()
    serializer = ExerciseLibrarySerializer(exercises, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


# -------------------------------------------------------exercise_library_detail_view------------------------------------------------------------

@api_view(['GET'])
def exercise_library_detail_view(request):
    exercise_pk = request.headers.get('pk')
    if not exercise_pk:
        return Response(
            {"error": "PK header is required"}, status=status.HTTP_400_BAD_REQUEST
        )

    exercise = get_object_or_404(ExerciseLibrary, pk=exercise_pk)
    serializer = ExerciseLibrarySerializer(exercise)
    return Response(serializer.data, status=status.HTTP_200_OK)


# -------------------------------------------------------exercise_library_create_view------------------------------------------------------------

@api_view(['POST'])
def exercise_library_create_view(request):
    serializer = ExerciseLibrarySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# -------------------------------------------------------exercise_library_partial_update_view------------------------------------------------------------

@api_view(['PATCH'])
def exercise_library_partial_update_view(request):
    exercise_pk = request.headers.get('pk')
    if not exercise_pk:
        return Response(
            {"error": "PK header is required"}, status=status.HTTP_400_BAD_REQUEST
        )

    exercise = get_object_or_404(ExerciseLibrary, pk=exercise_pk)
    serializer = ExerciseLibrarySerializer(exercise, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(
            {"message": "Exercise partially updated successfully", "data": serializer.data},
            status=status.HTTP_200_OK
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# -------------------------------------------------------exercise_library_delete_view------------------------------------------------------------

@api_view(['DELETE'])
def exercise_library_delete_view(request):
    exercise_pk = request.headers.get('pk')
    if not exercise_pk:
        return Response(
            {"error": "PK header is required"}, status=status.HTTP_400_BAD_REQUEST
        )

    exercise = get_object_or_404(ExerciseLibrary, pk=exercise_pk)
    exercise.delete()
    return Response(
        {"message": "Exercise deleted successfully"}, status=status.HTTP_204_NO_CONTENT
    )
