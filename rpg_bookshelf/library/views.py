from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from .forms import SearchForm
from .models import (
    Book,
    Author,
    Publisher,
    System,
    Shelf,
)
from django.views import View
from django.views.generic.edit import UpdateView, DeleteView, CreateView

# Create your views here.

class IndexView(View):
    def get(self,request):
        search_form = SearchForm()
        ctx = {
            'search_form': search_form
        }
        return render(request,'library/start.html', ctx)

    def post(self,request):
        search_form = SearchForm(data=request.POST)
        ctx = {
            'search_form': search_form
        }
        if search_form.is_valid():
            title  = search_form.cleaned_data['title']
            books = Book.objects.filter(title__icontains=title)
            ctx['results'] = books
        return render(request, 'library/search_results.html', ctx)

class SystemListView(View):
    def get(self,request):
        search_form = SearchForm()
        systems = System.objects.all().order_by('name')
        ctx = {'systems': systems,
               'search_form': search_form}
        return render(request, 'library/system_list.html', ctx)

class SystemView(View):
    def get(self,request,pk):
        system = System.objects.get(pk=pk)
        ctx = {'system': system}
        return render(request, 'library/system_details.html', ctx)

class AddSystemView(LoginRequiredMixin,CreateView):
    model = System
    fields = '__all__'
    success_url = '/systems/'

class ChangeSystemView(PermissionRequiredMixin,UpdateView):
    permission_required = ['library.change_system']
    model = System
    fields = '__all__'

class PublisherListView(View):
    def get(self,request):
        publishers = Publisher.objects.all().order_by('name')
        ctx = {'publishers': publishers}
        return render(request, 'library/publisher_list.html', ctx)

class PublisherView(View):
    def get(self,request,pk):
        publisher = Publisher.objects.get(pk=pk)
        ctx = {'publisher': publisher}
        return render(request, 'library/publisher_details.html', ctx)

class AddPublisherView(LoginRequiredMixin,CreateView):
    model = Publisher
    fields = '__all__'
    success_url = '/publishers/'

class ChangePublisherView(PermissionRequiredMixin,UpdateView):
    permission_required = ['library.change_publisher']
    model = Publisher
    fields = '__all__'

class AuthorListView(View):
    def get(self,request):
        authors = Author.objects.all().order_by('name')
        ctx = {'authors': authors}
        return render(request, 'library/author_list.html', ctx)

class AuthorView(View):
    def get(self,request,pk):
        author = Author.objects.get(pk=pk)
        ctx = {'author': author}
        return render(request, 'library/author_details.html', ctx)

class AddAuthorView(LoginRequiredMixin,CreateView):
    model = Author
    fields = '__all__'
    success_url = '/authors/'

class ChangeAuthorView(PermissionRequiredMixin,UpdateView):
    permission_required = ['library.change_author']
    model = Author
    fields = '__all__'

class BookListView(View):
    def get(self,request):
        books = Book.objects.all().order_by('title')
        ctx = {'books': books}
        return render(request, 'library/book_list.html', ctx)

class BookView(View):
    def get(self,request,pk):
        book = Book.objects.get(pk=pk)
        authors = Book.objects.get(pk=pk).authors.all()
        ctx = {'book': book,
               'authors': authors}
        return render(request, 'library/book_details.html', ctx)

class AddBookView(LoginRequiredMixin,CreateView):
    model = Book
    fields = '__all__'
    success_url = '/books/'

class ChangeBookView(PermissionRequiredMixin,UpdateView):
    permission_required = ['library.change_book']
    model = Book
    fields = '__all__'

class SearchView(View):

    def get(self,request):
        form = SearchForm()
        ctx = {
            'form': form
        }
        return render(request,'library/search_results.html', ctx)

    def post(self,request):
        form = SearchForm(data=request.POST)
        ctx = {
            'form': form
        }
        if form.is_valid():
            title  = form.cleaned_data['title']
            books = Book.objects.filter(title__icontains=title)
            ctx['results'] = books
        return render(request, 'library/search_results.html', ctx)

class ShelfView(View):
    def get(self,request,user_id):
        user = User.objects.get(id=user_id)
        shelf = Shelf.objects.filter(user=user).order_by('book')
        ctx = {
            'shelf': shelf,
            'user': user
        }
        return render(request, 'library/shelf.html', ctx)

class AddBookToShelfView(View):
    def get(self,request,book_id):
        user = request.user
        book = Book.objects.get(id=book_id)
        shelf = Shelf.objects.create(user=user, book=book)
        ctx = {
            'user': user,
            'book': book,
            'shelf': shelf
        }
        return redirect('../../shelf/{}'.format(user.id))

class DeleteBookFromShelf(DeleteView):
    model = Shelf
    success_url = '/'