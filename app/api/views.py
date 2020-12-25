from rest_framework import status
from rest_framework.response import responses
from rest_framework.decorators import api_view
from ..models import Data
from .serializers import DataSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView


@api_view(['GET' ])
def api_data_view(request , slug):
    try:
        info = Data.objects.get(slug=slug)
    except info.DoseNotExist:
        return responses(status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = DataSerializer(info)
        return responses(serializer.data)


@api_view(['PUT' ])
def api_update_data_view(request, slug):
    try:
        info = Data.objects.get(slug=slug)
    except info.DoseNotExist:
        return responses(status.HTTP_404_NOT_FOUND)
    if request.method == "PUT":
        serializer = DataSerializer(info, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data["success"] = "update success"
            return responses(data=data)
    return responses(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE' ])
def api_delete_data_view(request, slug):
    try:
        info = Data.objects.get(slug=slug)
    except info.DoseNotExist:
        return responses(status.HTTP_404_NOT_FOUND)

    if request.method == "DELETE":
        operation = info.delete()
        data = {}
        if operation:
            data["success"] = "delete success"
        else:
            data["failure"] = "delete failed"

            return responses(data=data)


@api_view(['POST', ])
def api_create_data_view(request, slug):
    try:
        info = Data.objects.get(slug=slug)
    except info.DoseNotExist:
        return responses(status.HTTP_404_NOT_FOUND)
    if request.method == "PUT":
        serializer = DataSerializer(info, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return responses(serializer.data, status=status.HTTP_201_CREATED)
    return responses(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ApiInfoListView(ListAPIView):
    queryset = Data.objects.all()
    serializer_class = DataSerializer
    pagination_class = PageNumberPagination
