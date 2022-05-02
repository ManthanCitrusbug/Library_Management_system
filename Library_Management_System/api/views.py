from multiprocessing import context
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from library_admin.serializers import BookSerializer, Issued_bookSerialize
from library_admin.models import Book, Issued_Book
from author.serializers import AuthorSerializer
from author.models import Author


class BookListAPIView(ModelViewSet):
    queryset = Book.objects.filter(deleted=False).order_by('id')
    serializer_class = BookSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class IssuedBookAPIView(ModelViewSet):
    queryset = Issued_Book.objects.all().order_by('id')
    serializer_class = Issued_bookSerialize
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class AuthorListAPIView(ModelViewSet):
    queryset = Author.objects.filter(deleted=False).order_by('id')
    serializer_class = AuthorSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]