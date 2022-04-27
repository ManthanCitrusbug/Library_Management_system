from django.db import models
from library_admin.models import Book

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    book = models.ManyToManyField(Book)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name