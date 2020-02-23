from rest_framework import serializers
from rest_framework.response import Response

from .models import Account

class HelloWorldSerializer(serializers.Serializer):
   name = serializers.CharField(max_length = 50)

class ProfileSerializer(serializers.ModelSerializer):
   class Meta:
      model = Account
      fields = ('id', 'email', 'username', 'password',)
      extra_kwargs = {'password': {'write_only': True}}

   def create(self, validated_data):
      user = Account(
         email = validated_data.get('email'),
         username = validated_data.get('username')
      )
      user.set_password(validated_data.get('password'))
      user.save()
      return user
   