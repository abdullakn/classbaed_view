from django.db import models
from django.db.models.aggregates import Count
from django.template.defaultfilters import slugify
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

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug=slugify(self.title)
        return super().save(*args,**kwargs)
