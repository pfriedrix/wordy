from django.db import models
from django.contrib.auth.models import AbstractUser

from .managers import UserManager


class User(AbstractUser):
    username = None
    email = models.CharField(unique=True, max_length=30)
    is_confirmed = models.BooleanField(default=False)
    confirmed_on = models.DateTimeField(null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        ordering = ('-date_joined',)

    def __repr__(self):
        return '<{self.email}>'


class Collection(models.Model):
    title = models.CharField(max_length=30)
    user = models.ForeignKey(User, models.CASCADE, related_name='collections')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def __repr__(self):
        return str(self.title)

    class Meta:
        ordering = ('-created_at',)

class Word(models.Model):
    title = models.CharField(max_length=255)
    translation = models.CharField(max_length=255)
    progress = models.IntegerField(default=0)
    collection = models.ForeignKey(Collection, models.CASCADE, related_name='words', related_query_name="word")
    user = models.ForeignKey(User, models.CASCADE, related_name='words')

    def __str__(self):
        return self.title

    def __repr__(self):
        return '<{self.title}>'

    class Meta:
        ordering = ('-progress',)

