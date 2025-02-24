from django.contrib import admin
from .models import Book

@admin.register(Book)
class AdminBook(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_publication', 'isbn')
    search_fields = ('title', 'author', 'isbn')
    list_filter = ('date_publication',)