from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from .models import Book, Borrowing, LibraryUser



#############  Login views ################
class StaffLoginView(LoginView):
    template_name = 'registration/staff_login.html'
    redirect_authenticated_user = True
    # Use the staff user authentication backend
    authentication_backend = 'django.contrib.auth.backends.ModelBackend'
    
    def form_valid(self, form):
        # Check if the user is staff before logging them in
        if self.request.user.is_staff:
            return super().form_valid(form)
        else:
            # Redirect to an error page if the user is not staff
            return redirect('not_staff_error')


class UserLoginView(LoginView):
    template_name = 'user_login.html'
    redirect_authenticated_user = True
    # Use the default authentication backend
    authentication_backend = None
    
    def form_valid(self, form):
        # Check if the user is not staff before logging them in
        if not self.request.user.is_staff:
            return super().form_valid(form)
        else:
            # Redirect to an error page if the user is staff
            return redirect('staff_error')



class StaffRequired(LoginRequiredMixin, UserPassesTestMixin):
    """Mixing for checking if user is logged in and is staff"""
    def test_func(self):
        return self.request.user.is_staff


############# STAFF VIEWS  #################
class BooksListStaffView(StaffRequired, ListView):
    """View for seeing books as library staff"""
    model=Book
    context_object_name='objects'
    template_name='books/book_list.html'
    paginate_by=12

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['detail_url'] = 'book_detail'
        context['page_title'] = 'List of all books' 
        return context


class BookDetailStaffView(StaffRequired, DetailView):
    """View for seeing single book as staff"""
    model=Book
    context_object_name='obj'
    template_name='books/book_detail.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['page_title'] = 'Details of a book',
        context['edit_url'] = 'book_update'
        return context


class BookCreateStaffView(CreateView):
    model = Book
    fields = '__all__'
    template_name = 'books/create_book.html'
    success_url = reverse_lazy('book_list')


class BookUpdateStaffView(UpdateView):
    """ Update view for an existing book"""
    model = Book
    fields = '__all__'
    template_name = 'books/edit_book.html'
    success_url = reverse_lazy('book_list')


class BookDeleteStaffView(DeleteView):
    """Delete view for an existing book"""
    model = Book
    template_name = 'book_confirm_delete.html'
    success_url = reverse_lazy('book_list')


class RegisterLibUserView(StaffRequired, CreateView):
    """View for staff members to register Library users"""
    template_name = 'registration/registration.html'



class AssignBookView(StaffRequired, CreateView):
    pass
    

############v NON-Staff views  ################
class BookListView(ListView):
    model=Book
    context_object_name='objects'
    template_name='books/book_list.html'
    paginate_by=12

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['detail_url'] = 'book_detail'
        context['page_title'] = 'List of all books' 
        return context
