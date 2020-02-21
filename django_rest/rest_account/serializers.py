from rest_framework import  serializers
from .models import Account,ProfileFeed


class HelloSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=30)


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'email', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = Account(
            email = validated_data['email'],
            username = validated_data['username']
        )
        user.is_staff = True
        user.set_password(validated_data['password'])
        user.save()
        return user

class ProfileFeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileFeed
        fields = ['id', 'feed_user', 'feed_text', 'created_on']
        extra_kwargs = {'feed_user': {'read_only': True}, 'created_on': {'read_only': True}}

    # def create(self, validated_data):
    #     user = ProfileFeed(
    #         feed_text= validated_data['feed_text']
    #     )
    #     user.save()
    #     return user
