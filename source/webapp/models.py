from django.db import models


# Create your models here.
class Quote(models.Model):
    text = models.TextField(
        max_length=200,
        null=False,
        blank=False,
        verbose_name="Текст"
    )
    author = models.CharField(
        max_length=20,
        null=False,
        blank=False,
        verbose_name="Автор"
    )
    email = models.EmailField(
        verbose_name="Почта"
    )
    rating = models.IntegerField(
        default=0,
        verbose_name="Рейтинг"
    )
    is_moderated = models.BooleanField(
        default=False,
        verbose_name="Статус"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания"
    )
