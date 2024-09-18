

from rest_framework import serializers
from .models import CarBrand, Book, Author, Car


class CarBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarBrand
        fields = '__all__'




class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['titel']


class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True)

    class Meta:
        model = Author
        fields = ['name', 'books']

    def create(self, validated_data):
        # Извлекаем данные для книг
        books_data = validated_data.pop('books')

        # Создаем автора
        author = Author.objects.create(**validated_data)

        # Создаем книги, связанные с этим автором
        for book_data in books_data:
            Book.objects.create(author=author, **book_data)

        return author


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'


