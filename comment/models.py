from django.db import models


class Comment(models.Model):
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    path = models.TextField()
    depth = models.IntegerField()
