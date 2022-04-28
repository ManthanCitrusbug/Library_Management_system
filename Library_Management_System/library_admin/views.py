from multiprocessing import context
from pyexpat import model
from re import template
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from author.models import Author
from library_admin.forms import AddBookForm, AdminLoginForm, AdminRegisterform, Issue_Book_Form, Issue_Book_Edit_Form
from django.contrib.auth.models import User
from django.views.generic import CreateView, TemplateView, ListView, UpdateView, DetailView, DeleteView
from django.contrib.auth import authenticate, login, logout
from library_admin.models import Book, Category, Issued_Book

from library_admin.models import Book

# Create your views here.

class IntexView(TemplateView):
    template_name = 'index.html'


class AdminRegisterView(CreateView):
    model = User
    form_class = AdminRegisterform
    template_name = 'admin_register.html'
    success_url = 'admin-login'


class AdminLoginView(View):
    def post(self,request):
        form = AdminLoginForm(request.POST)
        user_name = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=user_name,password=password)
        print(user)
        if user is not None: 
            login(request, user)
            return redirect('library_admin:admin-dashboard')
        else:
            return render(request,'admin_login.html',{'form':form}) 

    def get(self,request):
        form = AdminLoginForm()
        return render(request,'admin_login.html',{'form':form})


class AdminDashboardView(ListView):
    model = Book
    template_name = 'admin_dashboard.html'
    context = {}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = Book.objects.filter(deleted=False).order_by('id')
        return context


class AddBookView(CreateView):
    model = Book
    form_class = AddBookForm
    template_name = 'book/add_book.html'
    success_url = 'admin-dashboard'


class AdminLogoutView(View):
    def get(self,request):
        logout(request)
        return redirect('library_admin:index')


class EditBookView(UpdateView):
    model = Book
    form_class = AddBookForm
    template_name = 'book/add_book.html'
    success_url = reverse_lazy('library_admin:admin-dashboard')


class BookDetailView(DetailView):
    model = Book
    template_name = 'book/book_detail.html'


class DeleteBookView(View):
    def get(self, request, pk):
        book = Book.objects.get(id=pk)
        if book.deleted == False:
            return render(request, 'book/delete_book.html')
        return redirect('admin-dashboard')

    def post(self, request, pk):
        book = Book.objects.get(id=pk)
        book.deleted = True
        book.save()
        return redirect('library_admin:admin-dashboard')

    
class IssueBookView(CreateView):
    model = Issued_Book
    form_class = Issue_Book_Form
    template_name = 'book/issue_book.html'
    success_url = 'issued-books-list'


class IssuedBooksListView(ListView):
    model = Issued_Book
    template_name = 'book/issued_book_list.html'
    context = {}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = Issued_Book.objects.all().order_by('id')
        return context


class IssuedBookDetailsView(DetailView):
    model = Issued_Book
    template_name = 'book/issued_details.html'


class IssuedBookEditView(UpdateView):
    model = Issued_Book
    form_class = Issue_Book_Edit_Form
    template_name = 'book/edit_issued_book.html'
    success_url = reverse_lazy('library_admin:issued-books-list')

class IssuedBookDeleteView(DeleteView):
    model = Issued_Book
    template_name = 'book/delete_book.html'
    success_url = reverse_lazy('library_admin:issued-books-list')