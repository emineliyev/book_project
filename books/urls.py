from django.urls import path
from .views import IndexView, CreateReader, Readers, Books, add_new_book, GiveCreateBook, GiveBookList, GiveUpdateBook, \
    UpdateReader, delete_give, delete_reader, UpdateBook, delete_book


urlpatterns = [
    #  INDEX
    path('index/', IndexView.as_view(), name='index'),

    #  READER
    path('addreader/', CreateReader.as_view(), name='addreader'),
    path('readers/', Readers.as_view(), name='readers'),
    path('updatereader/<int:pk>/', UpdateReader.as_view(), name='updatereader'),
    path('readerdelete/<int:reader_id>/', delete_reader, name='readerdelete'),

    #  BOOKS
    path('books/', Books.as_view(), name='books'),
    path('addbook/', add_new_book, name='add_new_book'),
    path('booklist/<int:pk>/', GiveBookList.as_view(), name='booklist'),
    path('updatebook/<int:pk>/', UpdateBook.as_view(), name='updatebook'),
    path('deletebook/<int:book_pk>/', delete_book, name='deletebook'),

    #  GIVE BOOK
    path('updategivebook/<int:pk>', GiveUpdateBook.as_view(), name='updategivebook'),
    path('givebook/', GiveCreateBook.as_view(), name='givebook'),
    path('delete/<int:givebook_id>/', delete_give, name='delete'),
]
