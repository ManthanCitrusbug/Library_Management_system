from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=70)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    quantity = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    book = models.ManyToManyField(Book)

    def __str__(self):
        return self.name