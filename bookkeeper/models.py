from django.db import models


def publisher_upload_to(instance, filename):
    return 'uploads/publishers/%d/%s' % (instance, filename)

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
    return 'uploads/authors/%d/%s' % (instance, filename)

class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    photo = models.ImageField(upload_to=author_upload_to, blank=True, null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name


def cover_upload_to(instance, filename):
    return 'uploads/books/%d/%s' % (instance.pk, filename)

class Book(models.Model):
    title = models.CharField(max_length=120)
    publication_date = models.DateField(auto_now=False, auto_now_add=False)
    cover = models.ImageField(upload_to=cover_upload_to, blank=True, null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, related_name='books', on_delete=models.CASCADE)


    def __str__(self) -> str:
        return self.title

    def __repr__(self) -> str:
        return self.title