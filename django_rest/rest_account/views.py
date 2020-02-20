from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class HelloAPIView(APIView):
    def get(self, request):

        an_apiview = [
            'Uses HTTP methods as function (get, post, put, patch, delete)',
            'Full control over application logic',
            'Similar to traditional django view',
            'Is mapped manually to URLs'
        ]

        return Response({'message':'Hello APIView',
                        'api': an_apiview})
