from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from tinymce.models import HTMLField
from django.core.validators import MaxValueValidator
# import datetime as dt
import datetime

# Create your models here.
#book table
class Books(models.Model):
    DEPARTMENT = (
        ('ROM', 'Romantic'),
        ('REL', 'Religious'),
        ('FEM', 'Feminist'),
        ('COU', 'Courageous'),
    )
    isbn_no = models.CharField(max_length=20, blank=True)
    book_id = models.CharField(max_length=20)
    book_name = models.CharField(max_length=200)
    author_name = models.CharField(max_length=100)
    no_of_books = models.IntegerField()
    book_detail = models.TextField(default='text')
    department = models.CharField(max_length=3, choices=DEPARTMENT)
    rack_no = models.CharField(max_length=3)
    image = models.ImageField(upload_to = 'images/')

    def Claimbook(self):
        if self.no_of_books>1:
            self.no_of_books=self.no_of_books-1
            self.save()
        else:
            print("not enough books to Claim")

    def Addbook(self):
        self.no_of_books=self.no_of_books+1
        self.save()

    def delete_books(self):
        self.delete()

    @classmethod
    def search_by_name(cls,search_term):
        book=cls.objects.filter(name__icontains=search_term)
        return book

    def __str__(self):
        return self.book_name

class Profile(models.Model):
    image=models.ImageField(default='default.jpg', upload_to='profile_pics')
    bio=models.CharField(max_length=300)
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} Profile'

    def create_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

#borrower table
class BORROWER(models.Model):
    Fname = models.CharField(max_length=200)
    Lname = models.CharField(max_length=200)
    Address = models.CharField(max_length=200)
    phone = models.PositiveIntegerField(primary_key=True, validators=[MaxValueValidator(9999999999)])
    email = models.EmailField(max_length=70,blank=True, null= True, unique= True)

    def __str__(self):
        return self.Fname+" "+self.Lname


class Issue(models.Model):
    borrower_name = models.CharField(max_length=100)
    book_name = models.CharField(max_length = 200)
    book_id = models.CharField(max_length=20)
    issue_date = models.DateField(default=datetime.date.today)
    isbn_no = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.book_name

class Return(models.Model):
    return_date = models.DateField(default=datetime.date.today)
    borrower_name = models.CharField(max_length = 100)
    book_id = models.CharField(max_length=20)
    book_name= models.CharField(max_length=200)
    isbn_no = models.CharField(max_length=20)

    def __str__(self):
        return self.book_name
