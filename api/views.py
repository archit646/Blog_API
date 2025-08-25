from django.shortcuts import render
from rest_framework import viewsets
from blog.models import *
from .serializers import *
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.db.models import F
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import permissions

class RegisterView(APIView):
    def post(self,request):
        serializer=RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('User Registered Successfully',status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

        
class CategoryViewSet(viewsets.ModelViewSet):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
    authentication_classes=[JWTAuthentication]
    def get_permissions(self):
        if self.action in ['list','retrieve']:
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]

class PostViewSet(viewsets.ModelViewSet):
    queryset=Post.objects.all()
    serializer_class=PostSerializer
    authentication_classes=[JWTAuthentication]
    def get_permissions(self):
        if self.action in ['list','retrieve','recent','trending','releated']:
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        post = self.get_object()
        if post.author != self.request.user:
            raise permissions.PermissionDenied("You can't update this post.")
        serializer.save()

    def perform_destroy(self, instance):
        if instance.author != self.request.user:
            raise permissions.PermissionDenied("You can't delete this post.")
        instance.delete()
    
    def retrieve(self, request,*args,**kwargs):
        post=self.get_object()
        Post.objects.filter(id=post.id).update(views=F('views')+1)
        serializer=self.get_serializer(post)
        return Response(serializer.data)

    @action(detail=False,methods=['get'])
    def recent(self,request):
        
        posts=Post.objects.all().order_by('-created_at')[:5]
        serializer=self.get_serializer(posts,many=True)
        return Response(serializer.data)
    
    @action(detail=True,methods=['get'])
    def releated(self,request,pk=None):
        
        post=self.get_object()
        releated_posts=Post.objects.filter(category=post.category).exclude(id=post.id)[:5]
        serializer=self.get_serializer(releated_posts,many=True)
        return Response(serializer.data)
    
    @action(detail=False,methods=['get'])
    def trending(self,request):
        
        posts=Post.objects.all().order_by('-views')[:10]
        serializer=self.get_serializer(posts,many=True)
        return Response(serializer.data)
    
class CommentViewSet(viewsets.ModelViewSet):
    queryset=Comment.objects.all()
    serializer_class=CommentSerializer
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
