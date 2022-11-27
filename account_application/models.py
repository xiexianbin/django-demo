# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    nickname = models.CharField(max_length=50, blank=True)

    class Meta(AbstractUser.Meta):
        pass


class Author(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=80)


class Book(models.Model):
    name = models.CharField(max_length=20)
    # authors = models.ManyToManyField(Author)
    author = models.OneToOneField(Author)
