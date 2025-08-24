from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import *



router=DefaultRouter()
router.register('posts',PostViewSet,basename='posts')
router.register('categories',CategoryViewSet,basename='categories')
router.register('comments',CommentViewSet,basename='comments')

urlpatterns = [
    path('',include(router.urls)),
    path('register/',RegisterView.as_view()),
  
    
]
