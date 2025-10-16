from django.db import models

# Create your models here.
class Post(models.Model):
  title = models.CharField(max_length=100)


class Comment(models.Model):
  name = models.CharField(max_length=30)