from rest_framework import serializers
from rest_framework.response import Response

class HelloWorldSerializer(serializers.Serializer):
   name = serializers.CharField(max_length = 50)

   