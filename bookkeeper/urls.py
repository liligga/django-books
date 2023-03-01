from django.urls import path, include
from .views import book_list, book_detail, create_book, edit_book



urlpatterns = [
    path('', book_list, name='book_list'),
    path('<int:book_id>', book_detail, name='book_detail'),
    path('<int:book_id>/edit', edit_book, name='edit_book'),
    path('create', create_book, name='create_book'),
]
