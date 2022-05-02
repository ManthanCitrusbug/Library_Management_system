from rest_framework import serializers
from .models import Author
from library_admin.serializers import BookSerializer

class AuthorSerializer(serializers.ModelSerializer):
    book = BookSerializer(many=True, read_only=False)
    class Meta:
        model = Author
        fields = ['name', 'description', 'book']