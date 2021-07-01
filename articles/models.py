from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.deletion import CASCADE
from django.urls import reverse

class Category(models.Model):
    category = models.CharField(max_length=30)

    def __str__(self):
        return self.category


class Article(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=CASCADE)
    body = models.TextField()
    summary = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(blank=True, null = True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])
