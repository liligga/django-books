from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from .models import Publisher, Author, Book
from .forms import BookForm


def book_list(request: HttpRequest):
    objects = Book.objects.all()
    context = {
        'objects': objects,
        'page_title': 'List of all books' 
    }
    return render(request, 'books/book_list.html', context)


def book_detail(request: HttpRequest, book_id: int):
    obj = get_object_or_404(Book, pk=book_id)
    context = {
        'obj': obj,
        'page_title': 'Details of a book' 
    }
    return render(request, 'books/book_detail.html', context)


def create_book(request: HttpRequest):
    form = BookForm()
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            obj = form.save()
            print("BOOOOOK CREATED", obj.pk)
            return redirect('book_detail', book_id=obj.pk)
    context = {
        'form': form,
        'page_title': 'Create a book'
    }
    return render(request, 'books/create_book.html', context)


def edit_book(request: HttpRequest, book_id: int):
    obj = get_object_or_404(Book, pk=book_id)
    form = 'FORM'
    context = {
        'obj': obj,
        'form': form,
        'page_title': 'Edit a book '
    }
    return render(request, 'books/edit_book.html', context)

