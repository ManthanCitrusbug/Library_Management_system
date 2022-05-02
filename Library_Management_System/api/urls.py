from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from library_admin import APIviews
from author import APIviews as authorview

router = DefaultRouter()

router.register('book-api', APIviews.BookListAPIView, basename='book-api')
router.register('issued-book-api', APIviews.IssuedBookAPIView, basename='issued-book-api')
router.register('author-api', authorview.AuthorListAPIView, basename='author-api')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls')),
]
