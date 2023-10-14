from django.db import models


# Create your models here.
class Todo(models.Model):
    content = models.TextField()
    # is_done = models.BooleanField()


class Scrap(models.Model):
    title = models.TextField()
    url = models.TextField()
