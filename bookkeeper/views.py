from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Book, Borrowing, LibraryUser


class StaffRequired(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff


# STAFF VIEWS
class BooksView(StaffRequired, ListView):
    model=Book
    context_object_name='objects'
    template_name='books/book_list.html'
    paginate_by=12


class RegisterLibUser(StaffRequired, CreateView):
    template_name = 'registration/registration.html'
    