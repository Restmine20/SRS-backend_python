from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=20)
    reg_date = models.DateField()


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    create_date = models.DateField()
    text = models.TextField()
    likes_count = models.IntegerField()


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    create_date = models.DateField()
    text = models.TextField()
    likes_count = models.IntegerField()
