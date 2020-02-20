from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import status

from . import serializers

# Create your views here.


class HelloAPIView(APIView):
    serializer_class = serializers.HelloSerializer

    def get(self, request):
        an_apiview = [
            'Uses HTTP methods as function (get, post, put, patch, delete)',
            'Full control over application logic',
            'Similar to traditional django view',
            'Is mapped manually to URLs'
        ]

        return Response({'message': 'Hello APIView',
                        'api': an_apiview})

    def post(self, request):
        serializer = serializers.HelloSerializer(data= request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            return Response({'message': f"Hello {name}"})
        
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk= None):
        return Response({'method': 'put'})

    def patch(self, request, pk= None):
        return Response({'method': 'patch'})

    def delete(self, request, pk= None):
        return Response({'method': 'delete'})
