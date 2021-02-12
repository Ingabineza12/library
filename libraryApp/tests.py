from django.test import TestCase
from . models import *
# import datetime as dt
import datetime
# Create your tests here.


class ProfileTestClass(TestCase):
    '''
    images test method
    '''
    def setUp(self):
        self.user1 = User(username='deborah')
        self.user1.save()
        self.nature=Profile(2,user=self.user1,bio='A room without books is like a body without a soul.')
        self.nature.save_prof()


    def test_instance(self):
        self.assertTrue(isinstance(self.nature,Profile))


    def test_save_method(self):
        '''
        test image by save
        '''
        self.nature.save_prof()
        comm=Profile.objects.all()
        self.assertTrue(len(comm)>0)

    def test_delete_method(self):
        '''
        test of delete image
        '''

        Profile.objects.all().delete()


class BooksTestClass(TestCase):
    '''
    images test method
    '''
    def setUp(self):

        self.user1 = User(username='deborah')
        self.user1.save()
        self.image=Books(book_name='The wedding', author_name='Nicholas Sparks',department='ROM',rack_no="11",book_id="110")
        self.image.save_image()

    def test_instance(self):
        self.assertTrue(isinstance(self.image,Books))
    def test_save_method(self):
        '''
        test image by save
        '''
        self.image.save_image()
        images=Books.objects.all()
        self.assertTrue(len(images)>0)

    def test_delete_method(self):
        '''
        test of delete image
        '''
        Books.objects.all().delete()    
