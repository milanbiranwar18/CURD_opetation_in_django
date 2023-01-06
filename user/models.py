from django.db import models

# Create your models here.


class User(models.Model):
    user_name = models.CharField(max_length=300)
    date = models.DateTimeField(auto_now_add=True)

