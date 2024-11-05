from django.db import models
from django.contrib.auth import get_user_model
from apps.posts.models import Post
from django.core.exceptions import ValidationError

User = get_user_model()  

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'post')  

