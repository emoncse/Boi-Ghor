from django.shortcuts import render, get_object_or_404
from .models import Book


def home(request, book_id):
    book = get_object_or_404(Book, book_id=book_id)
    context = {
        'book': book
    }
    return render(request, 'book.html', context)