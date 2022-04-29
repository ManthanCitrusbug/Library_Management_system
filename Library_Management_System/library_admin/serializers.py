from dataclasses import field, fields
from rest_framework import serializers
from .models import Book, Issued_Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['name', 'description', 'quantity', 'category']

class Issued_bookSerialize(serializers.ModelSerializer):
    class Meta:
        model = Issued_Book
        fields = '__all__'