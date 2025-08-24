from django import forms
from .models import *
from ckeditor.widgets import CKEditorWidget
from django.contrib.auth.forms import UserCreationForm

class PostForm(forms.ModelForm):
    # content = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model=Post
        fields=['title','content','category','thumbnail']
        # widgets = {
        #     'title': forms.TextInput(attrs={
        #         'class': 'w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:border-indigo-500'
        #     }),
        #     'content': forms.Textarea(attrs={
        #         'class': 'w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:border-indigo-500',
        #         'rows': 6
        #     }),
        #     'thumbnail': forms.ClearableFileInput(attrs={
        #         'class': 'w-full'
        #     }),
        # }
        widgets={
            'title':forms.TextInput(attrs={'class':'w-full border'}),
            'category':forms.Select(attrs={'class':'w-full border'}),
            'thumbnail':forms.ClearableFileInput(attrs={'class':'w-full border'})
        }

class CustomSignUpForm(UserCreationForm):
    email=forms.EmailField(required=True)
    class Meta:
        model=User
        fields=['username','email','password1','password2']
        
        widgets={
            'username':forms.TextInput(attrs={'class':'w-full border'}),
            'email':forms.EmailInput(attrs={'class':'w-full border'}),
            'password1':forms.PasswordInput(attrs={'class':'w-full border'}),
            'password2':forms.PasswordInput(attrs={'class':'w-full border'})
        }
        
        
        