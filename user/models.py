from django.db import models

# Create your models here.


class User(models.Model):
    user_name = models.CharField(max_length=300)
    date = models.DateTimeField(auto_now_add=True)


class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_num = models.IntegerField()
    city = models.CharField(max_length=100)