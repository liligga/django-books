from django.urls import path, include
from .views import (
    book_list, 
    book_detail, 
    create_book, 
    edit_book,
    publisher_list,
    publisher_detail,
    edit_publisher
)



urlpatterns = [
    path('', book_list, name='book_list'),
    path('<int:book_id>', book_detail, name='book_detail'),
    path('<int:book_id>/edit', edit_book, name='edit_book'),
    path('create', create_book, name='create_book'),
    path('publishers', publisher_list, name='publisher_list'),
    path('publishers/<int:publisher_id>', publisher_detail, name='publisher_detail'),
    path('publishers/<int:publisher_id>/edit', edit_publisher, name='edit_publisher'),
]
