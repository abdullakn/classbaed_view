from django.db import models
from django.db.models.aggregates import Count

# Create your models here.

class Post(models.Model):
    post=models.CharField(max_length=200)


    def __str__(self):
        return self.post


class Book(models.Model):
    title=models.CharField(max_length=200)        
    genre=models.CharField(max_length=200)        
    slug=models.SlugField(max_length=200)        
    author=models.CharField(max_length=200)        
    isbn=models.CharField(max_length=200)     
    count=models.IntegerField(null=True,default=0)   
