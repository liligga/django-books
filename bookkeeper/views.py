from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.shortcuts import get_object_or_404, render
from django.urls import reverse


def book_list(request: HttpRequest):
    return render(request, 'books/book_list.html')


def book_detail(request: HttpRequest, book_id: int):
    return render(request, 'books/book_detail.html')


def create_book(request: HttpRequest):
    return render(request, 'books/create_book.html')


def edit_book(request: HttpRequest, book_id: int):
    return render(request, 'books/edit_book.html')

