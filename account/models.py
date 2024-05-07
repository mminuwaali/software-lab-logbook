from blog.models import Level
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    level = models.ForeignKey(Level, models.PROTECT, null=True, blank=True)
