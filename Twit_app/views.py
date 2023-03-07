from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.generics import RetrieveUpdateAPIView
from django.contrib.auth import get_user_model
from .models import Post, Like, Follow, Comment,User
from .serializers import PostSerializer, LikeSerializer, FollowSerializer, ProfileSerializer, CommentSerializers,UserSerializer,UserCreateSerializer

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from rest_framework.response import Response
from rest_framework import status,generics

#from rest_framework.decorators import api_view

#@api_view(["POST"])
#def Authmatic_author(request):

#    if request.method=="POST":
#        article["author"]=request.user


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        return super().get_queryset()


class LikeViewSet(ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer


class FollowViewSet(ModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer


class UserProfileView(RetrieveUpdateAPIView):
    """Control profile on endpoint /me/"""
    queryset = get_user_model().objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
    

#i need to create CommenViewSet
class CommentViewSet(ModelViewSet):
    queryset=Comment.objects.all()
    serializer_class=CommentSerializers
    #permission_classes=[IsAuthenticated]

class UserViewSet(ModelViewSet):
    serializer_class=UserSerializer
    queryset=User.objects.all()


    def get_permissions(self):
        if self.action=="create":
            self.permission_classes=[AllowAny]

        return super(UserViewSet,self).get_permissions()
    
    
    def get_serializer_class(self):
        serializer_map={
            "create":UserCreateSerializer,
            "list":UserSerializer
        }
        return serializer_map.get(self.action, UserSerializer)
    
    def get_queryset(self):
        return super().get_queryset()


#class MiniTwitViewSet(ModelViewSet):


class RelatedAPIView(generics.ListAPIView):

    def get(self, request, *args, **kwargs):
        user=request.user
        followed_user=Follow.objects.filter(followers=user).values_list('followings')
        print(followed_user)
        tweets=Post.objects.filter(authhor__in=followed_user)
        print(tweets)
        tweet_serializer=PostSerializer(tweets, many=True)
        return Response({"response":tweet_serializer.data, 'status':200}, status=status.HTTP_200_OK)
