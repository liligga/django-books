from django.db import models
from django.contrib.auth.models import User


def publisher_upload_to(instance, filename):
    return 'publishers/%s/%s' % (instance.name, filename)

class Publisher(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    image = models.ImageField(upload_to=publisher_upload_to, blank=True, null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return self.name


def author_upload_to(instance, filename):
    return 'authors/%s/%s' % (instance.name, filename)

class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    photo = models.ImageField(upload_to=author_upload_to, blank=True, null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name


class BookCategory(models.Model):
    name = models.CharField(max_length=150)
    descr = models.TextField()

    def __str__(self):
        return self.name


def cover_upload_to(instance, filename):
    return 'books/%s/%s' % (instance.title, filename)

class Book(models.Model):
    title = models.CharField(max_length=120)
    publication_date = models.DateField(auto_now=False, auto_now_add=False)
    cover = models.ImageField(upload_to=cover_upload_to, blank=True, null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    # author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
    authors = models.ManyToManyField(Author, related_name='books')
    categories = models.ManyToManyField(BookCategory, related_name='books')
    publisher = models.ForeignKey(Publisher, related_name='books', on_delete=models.CASCADE)


    def __str__(self) -> str:
        return self.title

    def __repr__(self) -> str:
        return self.title



class LibraryUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.first_name


class Borrowing(models.Model):
    class Statuses(models.TextChoices):
        LOST = ('lost', "Book is lost")
        BORROWED = ('bor', "Book is not retubed yet")
        RETURNED = ('ret', "Book is returned")
    borrower = models.ForeignKey(LibraryUser, on_delete=models.CASCADE, related_name='borrowings')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='borrowinngs')
    due_date = models.DateField()
    managed_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)


    def __str__(self):
        return f"User {self.borrower.user.username} borrowed a book {self.book.title} until {self.due_date}"