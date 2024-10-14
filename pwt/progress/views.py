from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Progress
from .serializers import ProgressSerializer

# -------------------------------------------------------progress_list_view------------------------------------------------------------

@api_view(['GET'])
def progress_list_view(request):
    progresses = Progress.objects.all()
    serializer = ProgressSerializer(progresses, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

# -------------------------------------------------------progress_detail_view------------------------------------------------------------

@api_view(['GET'])
def progress_detail_view(request):
    progress_id = request.headers.get('id')
    if not progress_id:
        return Response(
            {"error": "ID header is required"}, status=status.HTTP_400_BAD_REQUEST
        )

    progress = get_object_or_404(Progress, id=progress_id)
    serializer = ProgressSerializer(progress)
    return Response(serializer.data, status=status.HTTP_200_OK)

# -------------------------------------------------------progress_create_view------------------------------------------------------------


@api_view(['POST'])
def progress_create_view(request):
    serializer = ProgressSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# -------------------------------------------------------progress_partial_update_view------------------------------------------------------------

@api_view(['PATCH'])
def progress_partial_update_view(request):
    progress_id = request.headers.get('id')
    if not progress_id:
        return Response(
            {"error": "ID header is required"}, status=status.HTTP_400_BAD_REQUEST
        )

    progress = get_object_or_404(Progress, id=progress_id)
    serializer = ProgressSerializer(progress, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(
            {"message": "Progress partially updated successfully", "data": serializer.data},
            status=status.HTTP_200_OK
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# -------------------------------------------------------progress_delete_view------------------------------------------------------------

@api_view(['DELETE'])
def progress_delete_view(request):
    progress_id = request.headers.get('id')
    if not progress_id:
        return Response(
            {"error": "ID header is required"}, status=status.HTTP_400_BAD_REQUEST
        )

    progress = get_object_or_404(Progress, id=progress_id)
    progress.delete()
    return Response(
        {"message": "Progress deleted successfully"}, status=status.HTTP_204_NO_CONTENT
    )

