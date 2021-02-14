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
        ('INS', 'Inspiring'),
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
    def search_by_department(cls,search_term):
        book=cls.objects.filter(department__icontains=search_term)
        return book
    

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
