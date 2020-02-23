from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated

from .permissions import UpdateOwnProfileOnly, UpdateOwnFeedOnly
from . import serializers


from .models import Account,ProfileFeed
# Create your views here.

class HelloWorldAPIView(APIView):
    serializer_class = serializers.HelloWorldSerializer

    def get(self, request):

        hello_world_api_view = [
            "Gives you full control over application logic",
            "Perfect for dealing with complex logic",
            "While working with local files",
            "Calling other API's or services",
            "Each API view is manually mapped to URL"
        ]
        return Response({'message':'Message from API view', 'helloworldapiview': hello_world_api_view})

    def post(self, request):

        serializer = serializers.HelloWorldSerializer(data= request.data)
        if serializer.is_valid():
            name = serializer.data.get('name')
            return Response({'message': f"Hello {name}"})
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        return Response({'message':'Put HTTP method'})

    def patch(self, request, pk= None):
        return Response({'message': 'Patch HTTP method'})

    def delete(self, request, pk=None):
        return Response({'message': 'Delete HTTP method'})

class HelloWorldViewset(viewsets.ViewSet):
    serializer_class = serializers.HelloWorldSerializer

    def list(self, request):

        api_viewset= [
            'For simple CRUD operation on database',
            'API requires simple to no customization as well',
            'Want quick and simple API',
            'Your API is working with statndard data structures',
            'Automatically maps to URL using routers'
        ]

        return Response({'message': 'Hello World API Vieset', 'api': api_viewset})

    def create(self, request):
        serializer = serializers.HelloWorldSerializer(data = request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            return Response({'messgae': f"Hello {name}"})
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk =None):
        return Response({'message': 'HTTP method GET'})

    def update(self, request, pk = None):
        return Response({'message': 'HTTP method PUT'})

    def partial_update(self, request, pk = None):
        return Response({'message': 'HTTP method patch'})

    def destroy(self, request, pk= None):
        return Response({'message': 'HTTP method delete'})


class ProfileViewset(viewsets.ModelViewSet):
    serializer_class = serializers.ProfileSerializer
    queryset = Account.objects.all()
    permission_classes = (UpdateOwnProfileOnly,)
    authentication_classes = (TokenAuthentication, )
    filter_backends = (filters.SearchFilter,)
    search_fields = ('username', 'email',)

class LoginViewset(viewsets.ViewSet):
    serializer_class = AuthTokenSerializer

    def create(self, request):
        """"Obtain Temp Token"""
        return ObtainAuthToken().post(request)

class ProfileFeedViewset(viewsets.ModelViewSet):
    serializer_class = serializers.ProfileFeedSerializer
    queryset = ProfileFeed.objects.all()
    authentication_classes = (TokenAuthentication, )
    permission_classes = (UpdateOwnFeedOnly, IsAuthenticated, )
    filter_backends = (filters.SearchFilter,)
    search_fields = ('id', 'feed_text',)

    def perform_create(self, serializer):
        serializer.save(feed_user = self.request.user)