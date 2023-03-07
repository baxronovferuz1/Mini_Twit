from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Post, Like, Follow, Comment,File,User


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('id','username','first_name','last_name','email','password')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username')

class PostSerializer(serializers.ModelSerializer):
    liked_by_users = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'created_at', 'updated_at', 'author', 'like_count', 'liked_by_users','comments_count')


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ('id', 'user', 'post', 'created_at', 'updated_at')


class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = ('id', 'followers', 'followings', 'created_at', 'updated_at')


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = (
            'id', 'username', 'email', 'first_name', 'last_name', 'is_active', 
            'followers_count', 'following_count',
        )

class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields=[
            'author',
            'definition',
            'create_at',
        ]

class FileListSerializer(serializers.ModelSerializer):
    class Meta:
        model=File
        fields="__all__"