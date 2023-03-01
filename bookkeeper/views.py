from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import Publisher, Author, Book


def book_list(request: HttpRequest):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'books/book_list.html', context)


def book_detail(request: HttpRequest, book_id: int):
    book = get_object_or_404(Book, pk=book_id)
    context = {'book': book}
    return render(request, 'books/book_detail.html', context)


def create_book(request: HttpRequest):
    form = 'FORM'
    context = {'form': form}
    return render(request, 'books/create_book.html', context)


def edit_book(request: HttpRequest, book_id: int):
    book = get_object_or_404(Book, pk=book_id)
    context = {'book': book}
    return render(request, 'books/edit_book.html', context)

