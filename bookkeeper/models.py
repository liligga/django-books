from django.db import models


class Publisher(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=120)
    publication_date = models.DateField(auto_now=False, auto_now_add=False)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, related_name='books', on_delete=models.CASCADE)


    def __str__(self) -> str:
        return self.title

    def __repr__(self) -> str:
        return self.title