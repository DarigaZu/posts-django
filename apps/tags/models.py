from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class Tag(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    name = models.CharField(
        max_length=100,
        verbose_name='Название'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
    