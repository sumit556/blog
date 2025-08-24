from django.db import models
from django.contrib.auth.models import User   # built-in user model

# Category model for grouping posts
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)  # no duplicate names
    
    def __str__(self):
        return self.name

# Blog post model
class Post(models.Model):
    title = models.CharField(max_length=200)   # post title
    content = models.TextField()               # main content
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    tags = models.CharField(max_length=200, blank=True)  # simple tags stored as comma-separated
    created_at = models.DateTimeField(auto_now_add=True) # set once at creation
    updated_at = models.DateTimeField(auto_now=True)     # update whenever saved

    def __str__(self):
        return self.title
    
# Comments on blog posts
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author} on {self.post}"
