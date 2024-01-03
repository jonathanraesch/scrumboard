from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class UserStory(models.Model):
    title = models.CharField(max_length=100)
    story = models.TextField()
    author = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, default=None)
    pub_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
