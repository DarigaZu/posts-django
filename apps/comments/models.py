from django.db import models
from django.contrib.auth import get_user_model

from apps.posts.models import Post

User = get_user_model()

class Comment(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    text = models.TextField()
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comment',
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    def __str__(self):
        return self.text