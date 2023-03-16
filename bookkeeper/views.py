from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.shortcuts import get_object_or_404, render, redirect
from .models import Publisher, Author, Book
from .forms import BookForm, PublisherForm, AuthorForm
from django.contrib.auth.decorators import login_required



def book_list(request: HttpRequest):
    objects = Book.objects.all()
    context = {
        'objects': objects,
        'detail_url': 'book_detail',
        'page_title': 'List of all books' 
    }
    return render(request, 'books/book_list.html', context)


def book_detail(request: HttpRequest, book_id: int):
    obj = get_object_or_404(Book, pk=book_id)
    context = {
        'obj': obj,
        'page_title': 'Details of a book',
        'edit_url': 'edit_book'
    }
    return render(request, 'books/book_detail.html', context)


@login_required(login_url='user_login')
def create_book(request: HttpRequest):
    if Publisher.objects.count() < 1:
        # if there are no publishers to choose from
        return redirect('create_publisher')
    if Author.objects.count() < 1:
        # if there are no authors to choose from
        return redirect('create_author')
    form = BookForm()
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            obj = form.save()
            print("BOOOOOK CREATED", obj.pk)
            return redirect('book_detail', book_id=obj.pk)
    context = {
        'form': form,
        'page_title': 'Create a book',
        'create_url': 'create_book'
    }
    return render(request, 'books/create_book.html', context)


@login_required(login_url='user_login')
def edit_book(request: HttpRequest, book_id: int):
    obj = get_object_or_404(Book, pk=book_id)
    form = BookForm(instance=obj)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=obj)
        if form.is_valid():
            obj = form.save()
            return redirect('book_detail', book_id=obj.pk)
    context = {
        'obj': obj,
        'form': form,
        'page_title': 'Edit a book',
        'edit_url': 'edit_book'
    }
    return render(request, 'books/edit_book.html', context)


def publisher_list(request: HttpRequest):
    objects = Publisher.objects.all()
    context = {
        'objects': objects,
        'detail_url': 'publisher_detail',
        'page_title': 'List of all publishers' 
    }
    return render(request, 'books/book_list.html', context)


def publisher_detail(request: HttpRequest, publisher_id: int):
    obj = get_object_or_404(Publisher, pk=publisher_id)
    context = {
        'obj': obj,
        'page_title': 'Details of a publisher',
        'edit_url': 'edit_publisher'
    }
    return render(request, 'books/book_detail.html', context)


@login_required(login_url='user_login')
def create_publisher(request: HttpRequest):
    form = PublisherForm()
    if request.method == 'POST':
        form = PublisherForm(request.POST)
        if form.is_valid():
            obj = form.save()
            print("PUBL CREATED", obj.pk)
            return redirect('publisher_detail', publisher_id=obj.pk)
    context = {
        'form': form,
        'page_title': 'Create a publisher agency',
        'create_url': 'create_publisher'
    }
    return render(request, 'books/create_book.html', context)


@login_required(login_url='user_login')
def edit_publisher(request: HttpRequest, publisher_id: int):
    obj = get_object_or_404(Publisher, pk=publisher_id)
    form = PublisherForm(instance=obj)
    if request.method == 'POST':
        form = PublisherForm(request.POST, instance=obj)
        if form.is_valid():
            obj = form.save()
            return redirect('publisher_detail', publisher_id=obj.pk)
    context = {
        'obj': obj,
        'form': form,
        'page_title': 'Edit a publisher agency',
        'edit_url': 'edit_publisher'
    }
    return render(request, 'books/edit_book.html', context)


def author_list(request: HttpRequest):
    objects = Author.objects.all()
    context = {
        'objects': objects,
        'detail_url': 'author_detail',
        'page_title': 'List of all authors' 
    }
    return render(request, 'books/book_list.html', context)


def author_detail(request: HttpRequest, author_id: int):
    obj = get_object_or_404(Author, pk=author_id)
    context = {
        'obj': obj,
        'page_title': 'Details of a author',
        'edit_url': 'edit_author'
    }
    return render(request, 'books/book_detail.html', context)


@login_required(login_url='user_login')
def create_author(request: HttpRequest):
    form = AuthorForm()
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            obj = form.save()
            print("AUTHOOOOR CREATED", obj.pk)
            return redirect('author_detail', author_id=obj.pk)
    context = {
        'form': form,
        'page_title': 'Create an author',
        'create_url': 'create_author'
    }
    return render(request, 'books/create_book.html', context)


@login_required(login_url='user_login')
def edit_author(request: HttpRequest, author_id: int):
    obj = get_object_or_404(Author, pk=author_id)
    form = AuthorForm(instance=obj)
    if request.method == 'POST':
        form = AuthorForm(request.POST, instance=obj)
        if form.is_valid():
            obj = form.save()
            return redirect('author_detail', author_id=obj.pk)
    context = {
        'obj': obj,
        'form': form,
        'page_title': 'Edit an author',
        'edit_url': 'edit_author'
    }
    return render(request, 'books/edit_book.html', context)

