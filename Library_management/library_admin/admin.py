from django.contrib import admin
from .models import Book, Category, Author
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'quantity', 'category']

class AutherAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'quantity', 'category']

admin.site.register(Author,AutherAdmin)
admin.site.register(Book,BookAdmin)
admin.site.register(Category)