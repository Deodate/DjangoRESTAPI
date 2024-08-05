from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from . import models
from . import serializers
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import status  

class KigaliViewset(APIView):
    def get(self, request, id=None):
        if id:
            item = models.kigali.objects.get(id=id)
            serializer = serializers.Ki