from rest_framework import serializers

from .models import Book

class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'name', 'author_name', 'language', 'published_year', 'pages', 'created_date', 'created_by', 'updated_date', 'updated_by')

class AddBookSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('name', 'author_name', 'language', 'published_year', 'pages', 'created_by')

class UpdateBookSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'name', 'author_name', 'language', 'published_year', 'pages', 'updated_by')