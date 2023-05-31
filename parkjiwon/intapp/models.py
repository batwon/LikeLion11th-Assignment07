from django.db import models
from .models import Blogs

# Create your models here.

class Blogs(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    def __str__(req):
        return req.title