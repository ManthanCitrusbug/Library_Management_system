from asyncio.windows_events import NULL
from rest_framework import serializers

from author.models import Author
from .models import Book, Issued_Book
from datetime import date
# from author.serializers import AuthorSerializer

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['name', 'description', 'quantity', 'category']


class Issued_bookSerialize(serializers.ModelSerializer):
    book_ = BookSerializer(read_only=True, many=True)
    class Meta:
        model = Issued_Book
        fields = '__all__'

    def validate(self, data):
        issued_date = data.get('issued_date')
        email_data = data.get('email')
        book_name = data.get('book')
        re_book = data.get('return_date')
        if not book_name:
            if Issued_Book.objects.filter(email=email_data, book__name=book_name, return_date=None).exists():
                raise serializers.ValidationError("User has already issued this book.")
        if not re_book:
            if issued_date < date.today():
                raise serializers.ValidationError("Enter valid issue date.")
        if not book_name:
            book_instance = Book.objects.get(name=book_name, deleted=False)
            if book_instance.quantity == 0:
                raise serializers.ValidationError("Book is not available.")
        days = NULL
        if re_book != None:
            days = re_book - issued_date
            if days.days < 0:
                raise serializers.ValidationError("Enter valid return date.")
        return data

    def save(self, **kwargs):
        user = super().save()
        qun = Book.objects.get(name=user.book)
        if qun.quantity>0:
            x = qun.quantity - 1
            Book.objects.filter(name=user.book).update(quantity=x)
            user.save()
        return super().save(**kwargs)

    def update(self, instance, validated_data):
        qun = Book.objects.get(name=instance.book)
        x = qun.quantity + 1
        Book.objects.filter(name=instance.book).update(quantity=x)
        instance.save()
        return super().update(instance, validated_data)
