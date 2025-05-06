from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Post, Comment, Like

from django.contrib.auth.models import User

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ["post", "author", "text", "created_at"]


class PostSerializer(ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    likes_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ["id", "text", "image", "created_at", "comments", "likes_count"]

    def get_likes_count(self, instance):
        return instance.likes.count()

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'user', 'post', 'liked_at']

