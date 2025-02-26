from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"
        #fields = ["title", "author", "description", "date_publication", "isbn"] # 2nd way
