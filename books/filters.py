import django_filters
from django_filters.widgets import RangeWidget

from .models import Reader, Book, GiveBook


class BookGiveFilter(django_filters.FilterSet):
    class Meta:
        model = GiveBook
        fields = ('reader',)


class ReaderFilter(django_filters.FilterSet):
    first_name = django_filters.CharFilter(label='Ad', lookup_expr='icontains')
    last_name = django_filters.CharFilter(label='Soyad', lookup_expr='icontains')
    document_id = django_filters.CharFilter(label='FİN kod', lookup_expr='icontains')

    class Meta:
        model = Reader
        fields = (
            'first_name',
            'last_name',
            'document_id',
        )


class BookFilter(django_filters.FilterSet):
    book_name = django_filters.CharFilter(label='Kitab adı', lookup_expr='icontains')
    author = django_filters.CharFilter(label='Müəllif', lookup_expr='icontains')
    genre = django_filters.CharFilter(label='Janr', lookup_expr='icontains')

    class Meta:
        model = Book
        fields = (
            'book_name',
            'author',
            'genre',
        )
