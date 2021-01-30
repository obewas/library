from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.views.generic.base import View

from .models import Book, BookInstance, Author, Genre, Language

# Create your views here.
def index(request):
    #objects counts
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    #available books
    num_instances_available = BookInstance.objects.filter(status='a').count()
    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1
    num_authors = Author.objects.count()
    num_genres = Genre.objects.count()
    books_django = Book.objects.filter(title='Django')
    context = {
        'num_books':num_books, 'num_instances':num_instances,'num_instances_available':num_instances_available, 'num_authors':num_authors,'num_genres':num_genres,
        'books_django':books_django,'num_visits':num_visits,
    }
    return render(request, 'index.html', context)

class BookListView(generic.ListView):
    model = Book
    context_object_name = 'book_list'
   # queryset = Book.objects.filter(title='Django')
    template_name = 'catalog/book_list.html'



class BookDetailView(generic.ListView):
    model = Book

    def book_detail_view(request, primary_key):
        try:
            book = get_object_or_404(Book, pk=primary_key)
        except Book.DoesNotExist:
            raise Http404('Book does not exist')

        return render(request, 'catalog/book_detail.html', context={'book': book})

    class MyView(LoginRequiredMixin, View):
        login_url = '/login/'
        redirect_field_name = 'redirect_to'

class LoanedBooksByUserListView(LoginRequiredMixin, generic.ListView):
    model = BookInstance
    template_name = 'catalog/book_instance_list_borrowed_user.html'
    paginate_by = 10

    def get_queryset(self):

        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalog:index')
    form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form':form})
