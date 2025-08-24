from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Category(models.Model):
    name=models.CharField(max_length=30)
    def __str__(self):
        return self.name
    
class Post(models.Model):
    title=models.CharField(max_length=100,unique=True)
    content=RichTextField()
    created_at=models.DateField(auto_now_add=True)
    views=models.IntegerField(default=0)
    author=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    thumbnail=models.ImageField(upload_to='images/',default="")
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    post=models.ForeignKey(Post,related_name='comments',on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering=['-created_at']
    def __str__(self):
        return f'Comment by {self.user.username} on {self.post.title}' 
    
