from rest_framework import serializers
from rest_framework.response import Response

from .models import Account, ProfileFeed

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
      user.is_staff = True
      user.set_password(validated_data.get('password'))
      user.save()
      return user

class ProfileFeedSerializer(serializers.ModelSerializer):
   class Meta:
      model = ProfileFeed
      fields = '__all__'
      extra_kwargs = {'feed_user': {'read_only': True}}
