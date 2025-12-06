from rest_framework import serializers
from api.models import *
from django.contrib.auth.models import User

class RegisterSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)
    class Meta:
        model=User
        fields=['username','email','password']
        
    def create(self, validated_data):
        user=User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password']
        )
        return user

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','username']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'

class CommentSerializer(serializers.ModelSerializer):
    user=AuthorSerializer(read_only=True)
    # post=PostSerializer()
    class Meta:
        model=Comment
        fields=['id','user','content','post','created_at']

class PostSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    comments=CommentSerializer(many=True,read_only=True)
    category = serializers.SlugRelatedField(
        slug_field='name',
        queryset=Category.objects.all()
    )
    class Meta:
        model=Post
        fields=['id','title','content','created_at','views','author','category','thumbnail','comments']

