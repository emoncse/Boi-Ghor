from django.contrib import admin
from .models import Author, Category, Genre, Book, Review

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'category', 'genre', 'price')
    search_fields = ('name', 'author__name', 'category__name', 'genre__name')
    list_filter = ('author', 'category', 'genre')

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('book', 'reviewer_name', 'rating')
    search_fields = ('book__name', 'reviewer_name')
    list_filter = ('book',)
