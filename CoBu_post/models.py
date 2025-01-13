from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("home")


class Post(models.Model):

    PLATFORM_CHOICES = [('PC', 'PC'),
    ('Playstation', 'Playstation'),
    ('Xbox', 'Xbox'), 
    ('Nintendo', 'Nintendo'),
    ]

    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=225)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(default='This is a default body content.')
    post_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=255, default='uncategorised')
    platform = models.CharField(max_length=255, 
    choices=PLATFORM_CHOICES, 
    default='PC')
    likes = models.ManyToManyField(User, related_name='blog_posts')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse("post-details", args=[str(self.id)])
    