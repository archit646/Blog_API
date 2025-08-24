from django.urls import path
from .views import *
urlpatterns = [
    path('',HomePageView.as_view(),name='home'),
    path('<int:pk>/',DetailPage.as_view(),name='detail'),
    path('createpost/',CreatePostView.as_view(),name='createpost'),
    path('signup/',SignUpView.as_view(),name='signup')
]
