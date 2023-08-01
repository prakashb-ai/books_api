from django.db import models

# Create your models here.

class Book(models.Model):
    Book_number =models.IntegerField()
    Book_name = models.CharField(max_length=50)
    Book_author_name = models.CharField(max_length=50)
