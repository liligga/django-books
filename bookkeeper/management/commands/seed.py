from django.core.management.base import BaseCommand, CommandError
import factory
from datetime import date
from random import randint as rnd
from bookkeeper.models import Book, Author, Publisher
from faker import Faker
from django.contrib.auth import get_user_model


fake = Faker("ru_RU")


class PublisherFactory(factory.django.DjangoModelFactory):
    name = factory.Faker("company")
    address = factory.Faker("address")

    class Meta:
        model = Publisher


class AuthorFactory(factory.django.DjangoModelFactory):
    name = factory.Faker("name")
    email = factory.Faker("email")
    
    class Meta:
        model = Author


class BookFactory(factory.django.DjangoModelFactory):
    title = factory.LazyFunction(lambda: ' '.join(fake.words()).capitalize())
    publication_date = date(
        year=rnd(2021, 2023),
        month=rnd(3,12),
        day=rnd(1, 30))
    # authors = factory.Iterator(Author.objects.all())
    publisher = factory.Iterator(Publisher.objects.all())

    class Meta:
        model = Book


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        User = get_user_model()
        if User.objects.exists():
            return
        User.objects.create_superuser(username="admin", password="admin", email="admin@mail.ru")
        self.stdout.write(self.style.SUCCESS("Admin user created successfuly(admin: admin)"))


        with factory.Faker.override_default_locale('ru_RU'):
            publ = PublisherFactory.create_batch(20)
            authr = AuthorFactory.create_batch(20)
            # books are created only after authors and publishers are created
            books = BookFactory.create_batch(55)

        self.stdout.write(self.style.SUCCESS("Fake data created successfuly"))
