from django.contrib import admin
from library_admin.models import Book, Category
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'quantity', 'category']

admin.site.register(Book, BookAdmin)
admin.site.register(Category)
