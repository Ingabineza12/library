from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from .forms import *
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def home(request):
    return render(request,'home.html')


@login_required(login_url='/login/')
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/registration_form.html', {'form': form})


@login_required(login_url='/accounts/login/')
def myprofile(request,username=None):
    current_user=request.user
    profile=Profile.objects.filter(user=current_user)
    if not username:
        username=request.user.username
        images=Profile.objects.filter(bio=username)
    return render(request,'myprofile.html',locals(),{"profile":profile})


@login_required(login_url='/accounts/login/')
def profile_edit(request):
    current_user=request.user
    if request.method=='POST':
        form=UpdatebioForm(request.POST,request.FILES)
        if form.is_valid():
            image=form.save(commit=False)
            image.user=current_user
            image.save()
        return redirect('home')
    else:
        form=UpdatebioForm()
    return render(request,'registration/profile_edit.html',{"form":form})


@login_required(login_url='/login/')
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('all_books')

    else:
        form = BookForm()

    return render(request, 'add_book.html', {'form': form})

@login_required(login_url='/login/')
def all_books(request):
    books = Books.objects.order_by('department')
    query = request.GET.get('q')
    if query:
        books = Books.objects.filter(Q(book_name__icontains=query) | Q(author_name__icontains=query) | Q(book_detail__icontains=query) | Q(department__icontains=query))
    else:
        books = Books.objects.order_by('department')
    return render(request, 'all_books.html', {'books': books})

# @login_required(login_url='login')
# def all_books(request):
#     books = Books.objects.all()
#     return render(request,'all_books.html',{'books':books})

@login_required(login_url='login')
def book(request,hood_id):
    current_user = request.user
    book_name = current_user.profile.hood
    book = Book.objects.get(id=book_id)
    return render(request,'book.html',{"book_name":book_name,"author_name":author_name,"book_detail":book_detail})

@login_required(login_url='/login/')
def view_issue(request):
    issue = Issue.objects.order_by('borrower_name', 'issue_date')
    return render(request, 'view_issue.html', {'issue': issue})

@login_required(login_url='/login/')
def new_issue(request):
    if request.method == 'POST':
        form = IssueForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['borrower_id']
            book = form.cleaned_data['isbn_no']
            form.save(commit=True)
            books = Books.objects.get(isbn_no=book)
            Books.Claimbook(books)
            return redirect('new_issue')
    else:
        form = IssueForm()
    return render(request, 'new_issue.html', {'form': form})


@login_required(login_url='/login/')
def return_book(request):
    if request.method == 'POST':
        form = ReturnForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            book = form.cleaned_data['isbn_no']
            books = Books.objects.get(isbn_no=book)
            Books.Addbook(books)
            Issue.objects.filter(isbn_no=book).delete()
            return redirect('return_book')
    else:
        form = ReturnForm()
    return render(request, 'return_book.html', {'form': form})

def search_books(request):
    if 'book' in request.GET and request.GET["book"]:
        search_term=request.GET.get("book")
        searched_books=Book.search_by_name(search_term)
        message=f"{search_term}"

        return render(request,'all_news/search.html',{"message":message,"searched_books":searched_books})

    else:
        message="You haven't searched for any term"
        return render(request, 'all_news/search.html',{"message":message})
