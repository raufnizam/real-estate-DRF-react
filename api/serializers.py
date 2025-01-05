from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Tag, Property, Comments

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class PropertySerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    total_likes = serializers.ReadOnlyField()

    class Meta:
        model = Property
        fields = '__all__'

class CommentsSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Comments
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']
