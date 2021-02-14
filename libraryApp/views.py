from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from .forms import *
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def index(request):
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
    # current_user=request.user
    if request.method == 'POST':
        form = BookForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('all_books')

    else:
        form = BookForm()

    return render(request,'registration/add_book.html',{'form':form})



# @login_required(login_url='/accounts/login/')
# def all_books(request):
#     books = Books.objects.order_by('department')
#     query = request.GET.get('q')
#     if query:
#         books = Books.objects.filter(Q(book_name__icontains=query) | Q(author_name__icontains=query) | Q(book_detail__icontains=query) | Q(department__icontains=query))
#     else:
#         books = Books.objects.order_by('department')
#     return render(request, 'all_books.html', {'books': books})


@login_required(login_url='/login/')
def all_books(request):
    books = Books.objects.all()
    return render(request,'all_books.html',{'books':books})

@login_required(login_url='login')
def book(request,book_id):
    books = Books.objects.filter(id=book_id)
    return render(request,'book.html',{'books':books})

# def one_art(request,id):
#     ones_art = Art.objects.filter(id = id)
#     return render(request,'art.html',{"ones_art":ones_art,})

def search_books(request):
    if 'department' in request.GET and request.GET["department"]:
        search_term=request.GET.get("department")
        searched_books=Books.search_by_department(search_term)
        message=f"{search_term}"

        return render(request,'search.html',{"message":message,"searched_books":searched_books})

    else:
        message="You haven't searched for any term"
        return render(request, 'search.html',{"message":message})
