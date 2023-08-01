from datetime import date
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import ProtectedError
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.contrib import messages
from .filters import BookGiveFilter, ReaderFilter, BookFilter
from django.views.generic import CreateView, ListView, UpdateView, DetailView
from .forms import CreateReaderForm, CreateBookForm, GiveBookForm
from .models import Reader, Book, GiveBook


#  INDEX
class IndexView(ListView):
    model = GiveBook
    template_name = 'books/index.html'
    context_object_name = 'givebooks'

    def get_queryset(self):
        qs = self.model.objects.all()
        my_filter = BookGiveFilter(self.request.GET, queryset=qs)
        return my_filter.qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['counter'] = GiveBook.objects.count()
        context['my_filter'] = BookGiveFilter(self.request.GET, queryset=self.get_queryset())
        context['today'] = date.today()
        return context


#  READER
class Readers(ListView):
    model = Reader
    template_name = 'books/readers.html'
    context_object_name = 'readers'

    def get_queryset(self):
        qs = self.model.objects.all()
        my_filter = ReaderFilter(self.request.GET, queryset=qs)
        return my_filter.qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['counter'] = Reader.objects.count()
        context['my_filter'] = ReaderFilter(self.request.GET, queryset=self.get_queryset())
        return context


class CreateReader(SuccessMessageMixin, CreateView):
    form_class = CreateReaderForm
    template_name = 'books/addreader.html'
    success_url = reverse_lazy('readers')
    success_message = 'Oxuyucu uğurla əlavə edildi!'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class UpdateReader(SuccessMessageMixin, UpdateView):
    form_class = CreateReaderForm
    model = Reader
    template_name = 'books/updatereader.html'
    success_url = reverse_lazy('readers')
    success_message = 'Oxuyucunun məlumatları uğurla dəyişdirildi!'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def delete_reader(request, reader_id):
    reader = Reader.objects.get(id=reader_id)
    try:
        reader.delete()
        messages.success(request, 'Oxuyucu uğurla silindi!')

    except ProtectedError:
        messages.error(request, 'Oxuyucu kitabı təhvil verməyib!')
    return redirect('readers')


#  BOOK
class Books(ListView):
    model = Book
    template_name = 'books/books.html'
    context_object_name = 'books'

    def get_queryset(self):
        qs = self.model.objects.all()
        my_filter = BookFilter(self.request.GET, queryset=qs)
        return my_filter.qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['counter'] = Book.objects.count()
        context['my_filter'] = BookFilter(self.request.GET, queryset=self.get_queryset())
        return context


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


def add_new_book(request):
    if request.method == 'POST':
        form = CreateBookForm(request.POST)
        if form.is_valid():
            book_name_data = request.POST.get('book_name')
            author_data = request.POST.get('author')
            genre_data = request.POST.get('genre')
            form = Book(book_name=book_name_data, author=author_data, genre=genre_data)
            form.save()
            return JsonResponse({'status': 'Good'})
        else:
            return JsonResponse({'status': 'error'})
    else:
        form = CreateBookForm()
        context = {
            'form': form
        }
    return render(request, 'books/addbook.html', context=context)



# class CreateBook(SuccessMessageMixin, CreateView):
#     form_class = CreateBookForm
#     template_name = 'books/addbook.html'
#     success_url = reverse_lazy('books')
#     success_message = 'Yeni kitab uğurla əlavə edildi!'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         return context


class UpdateBook(SuccessMessageMixin, UpdateView):
    form_class = CreateBookForm
    model = Book
    template_name = 'books/updatebook.html'
    success_url = reverse_lazy('books')
    success_message = 'Kitab məlimatları uğurla dəyişdirildi!'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def delete_book(request, book_pk):
    book = Book.objects.get(id=book_pk)
    try:
        book.delete()
        messages.success(request, 'Kitab uğurla silindi!')
    except ProtectedError:
        messages.error(request, 'Kitab icarədədir!')
    return redirect('books')


# **********************************
#  GIVE BOOK
class GiveCreateBook(SuccessMessageMixin, CreateView):
    form_class = GiveBookForm
    template_name = 'books/givebook.html'
    success_url = reverse_lazy('index')
    success_message = 'Əməliyyat uğurla icra olundu!'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class GiveUpdateBook(UpdateView):
    form_class = GiveBookForm
    model = GiveBook
    template_name = 'books/updategivebook.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class GiveBookList(DetailView):
    model = GiveBook
    template_name = 'books/booklist.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def delete_give(request, givebook_id):
    give = GiveBook.objects.get(id=givebook_id)
    give.delete()
    messages.success(request, 'Kitab təhvil verildi!')
    return redirect('index')
