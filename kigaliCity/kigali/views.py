# from rest_framework import viewsets
# from django.shortcuts import get_object_or_404
# from . import models
# from . import serializers
# from rest_framework.views import APIView
# from rest_framework.response import Response 
# from rest_framework import status  

# class KigaliViewset(APIView):
#     def get(self, request, id=None):
#         if id:
#             item = models.kigali.objects.get(id=id)
#             serializer = serializers.KigaliSerializer(item)
#             return Response({"status", "data": serializer.data}, status=status.HTTP_200_OK)

#             items = models.Kigali.objects.all()
#             serializer = serializers.KigaliSerializer(items, many=True)
#             return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

#     def post(self, request):
#         serializer = serializers.KigaliSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
#             else: 
#                 return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

#             def patch(self, request, id=None):
#                 item = models.Kigali.objects.get(id=id)
#                 serializer = serializers.KigaliSerializer(item, data=request.data, partial=True)
#                 if serializer.is_valid():
#                     serializer.save()
#                     return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
#                     else:
#                     return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

#                     def delete(self, request, id=None):
#                         item = models.Kigali.objects.filter(id=id)
#                         print(item)
#                         item.delete()
#                         return Response({"status": "success", "data": "Item Delete"})

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Kigali
from rest_framework import viewsets
from .serializers import KigaliSerializer

class KigaliViewset(APIView):
    def get(self, request, id=None):
        if id:
            item = Kigali.objects.filter(id=id).first()  # Use filter().first() to avoid exceptions if item doesn't exist
            if item is None:
                return Response({"status": "error", "data": "Item not found"}, status=status.HTTP_404_NOT_FOUND)
            serializer = KigaliSerializer(item)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            items = Kigali.objects.all()
            serializer = KigaliSerializer(items, many=True)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = KigaliSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id=None):
        if id:
            item = Kigali.objects.filter(id=id).first()  # Use filter().first() to avoid exceptions if item doesn't exist
            if item is None:
                return Response({"status": "error", "data": "Item not found"}, status=status.HTTP_404_NOT_FOUND)
            serializer = KigaliSerializer(item, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"status": "error", "data": "ID not provided"}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None):
        if id:
            item = Kigali.objects.filter(id=id).first()  # Use filter().first() to avoid exceptions if item doesn't exist
            if item is None:
                return Response({"status": "error", "data": "Item not found"}, status=status.HTTP_404_NOT_FOUND)
            item.delete()
            return Response({"status": "success", "data": "Item deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        return Response({"status": "error", "data": "ID not provided"}, status=status.HTTP_400_BAD_REQUEST)
