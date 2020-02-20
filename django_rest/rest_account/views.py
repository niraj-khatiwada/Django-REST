from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
from rest_framework.authentication import TokenAuthentication

from . import serializers
from .models import Account

from. import permission

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


class HelloViewSet(viewsets.ViewSet):
    serializer_class = serializers.HelloSerializer
    def list(self, request):

        api_viewset= [
                        "Uses action (list, retrieve, create, update, partial_update, destroy) ",
                        "Automatically maps to URL's using Routers",
                        "Provides more functionality with less code"
        ]

        return Response({'message': 'Hello', 'api_viewset': api_viewset})

    def create(self, request):
        serializer = serializers.HelloSerializer(data= request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            return Response({'message': f"Hello { name }"})
        else:
            return Response(status.errors, status = status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk = None):
        return Response({'method': 'Retrieve'})

    def update(self, request, pk = None):
        return Response({'method': 'Update'})

    def partial_update(self, request, pk =None):
        return Response({'method': 'Partial Update'})

    def destroy(self, request, pk=None):
        return Response({'method': 'Destroy'})


class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ProfileSerializer
    queryset = Account.objects.all()

    authentication_classes = (TokenAuthentication,)
    permission_classes = (permission.UpdateOwnProfile,)


