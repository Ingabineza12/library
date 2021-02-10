from django.conf.urls import url,include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url(r'^$', views.index, name='home'),
    url(r'^all_books/$', views.all_books, name='all_books'),
    url(r'^book/(\d+)',views.book,name ='book'),
    url(r'^book/add/$', views.add_book, name='add_book'),
    url(r'^delete_book/$', views.ViewDeletePost, name='delete_book'),
    url(r'^edit/profile$',  views.profile_edit,name='profile_edit'),
    url(r'^myprofile/$',  views.myprofile,name='myprofile'),
    url(r'^issue/$', views.view_issue, name='view_issue'),
    url(r'^issue/new/$', views.new_issue, name='new_issue'),
    url(r'^return_book/$', views.return_book, name='return_book'),
    url(r'^search/$',  views.search_books,name='search_books'),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
