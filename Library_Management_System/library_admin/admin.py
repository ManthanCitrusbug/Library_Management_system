from django.contrib import admin
from library_admin.models import Book, Category, Issued_Book
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'quantity', 'category']

class Issued_Book_Admin(admin.ModelAdmin):
    list_display = ['username', 'book', 'email', 'issued_date', 'return_date', 'total_charge']

admin.site.register(Book, BookAdmin)
admin.site.register(Issued_Book, Issued_Book_Admin)
admin.site.register(Category)
