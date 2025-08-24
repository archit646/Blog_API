from django.shortcuts import render
from django.views.generic import *
from .models import *
from .forms import *
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class HomePageView(ListView):
    model=Post
    template_name='home.html'
    context_object_name='posts'
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['recent']=Post.objects.order_by('-created_at')[:5]
        context['categories']=Category.objects.all()
        context['trending']=Post.objects.order_by('-views')[:5]
        return context
    def get_queryset(self):
        queryset=Post.objects.all()
        category=self.request.GET.get('category')
        if category:
            queryset=queryset.filter(category__name__iexact=category)
        return queryset
    
class DetailPage(DetailView):
    model=Post
    template_name='detailpage.html'
    context_object_name='post'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        post=self.object
        context['releated']=Post.objects.filter(category=post.category).exclude(id=post.id)[:5]
        return context
    
class CreatePostView(LoginRequiredMixin,CreateView):
    model=Post
    template_name='createpost.html'
    form_class=PostForm
    success_url=reverse_lazy('home')
    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)

class SignUpView(CreateView):
    model=User
    template_name='signup.html'
    form_class=CustomSignUpForm
    success_url=reverse_lazy('login')
    

    
    
        
    
