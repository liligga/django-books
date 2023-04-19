from django.urls import path
# from .old_views import (
#     author_detail,
#     author_list,
#     book_list, 
#     book_detail,
#     create_author, 
#     create_book,
#     edit_author, 
#     edit_book,
#     publisher_list,
#     publisher_detail,
#     edit_publisher,
#     create_publisher
# )

from .views import (
    BooksListStaffView,
    BookListView,
    BookCreateStaffView,
    BookDeleteStaffView,
    BookDetailStaffView,
    BookUpdateStaffView,
    StaffLoginView,
    UserLoginView
)


urlpatterns = [
    path('', BookListView.as_view(), name='book_list_for_user'),
    path('books', BooksListStaffView.as_view(), name='book_list'),
    path('books/create/', BookCreateStaffView.as_view(), name='book_create'),
    path('books/<int:pk>/', BookDetailStaffView.as_view(), name='book_detail'),
    path('books/<int:pk>/update/', BookUpdateStaffView.as_view(), name='book_update'),
    path('books/<int:pk>/delete/', BookDeleteStaffView.as_view(), name='book_delete'),
    path('login/staff/', StaffLoginView.as_view(), name='staff_login'),
    path('login/normal/', UserLoginView.as_view(), name='lib_user_login'),
]


# urlpatterns = [
#     path('', book_list, name='book_list'),
#     path('<int:book_id>', book_detail, name='book_detail'),
#     path('<int:book_id>/edit', edit_book, name='edit_book'),
#     path('create', create_book, name='create_book'),
#     path('publishers', publisher_list, name='publisher_list'),
#     path('publishers/<int:publisher_id>', publisher_detail, name='publisher_detail'),
#     path('publishers/<int:publisher_id>/edit', edit_publisher, name='edit_publisher'),
#     path('publishers/create', create_publisher, name='create_publisher'),
#     path('authors', author_list, name='author_list'),
#     path('authors/<int:author_id>', author_detail, name='author_detail'),
#     path('authors/<int:author_id>/edit', edit_author, name='edit_author'),
#     path('authors/create', create_author, name='create_author'),
# ]
