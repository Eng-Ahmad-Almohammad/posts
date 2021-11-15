from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Type(models.Model):
    type = models.CharField(max_length=255, unique=True)
    def __str__(self):
        return self.type

    class Meta:
        verbose_name = "Type"
        verbose_name_plural = "Types"
class Posts(models.Model):
    poster = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    body = models.TextField()
    type = models.ForeignKey(Type, on_delete=models.CASCADE)

    def __str__(self):
        return self.body

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

class Comments(models.Model):
    commenter = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name='comments')   
    
    def __str__(self):
        return self.body

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"