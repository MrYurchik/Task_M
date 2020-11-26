from django.contrib.auth.models import User
from django.db import models


class TaskOrder(models.Model):
    title = models.CharField(max_length=180)
    description = models.CharField(max_length=320)
    implementation = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

