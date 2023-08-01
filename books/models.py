from django.db import models
from books.signals import get_number


class Book(models.Model):
    book_name = models.CharField(max_length=60, verbose_name='Kitab adı', unique=True)
    author = models.CharField(max_length=60, verbose_name='Müəllif')
    genre = models.CharField(max_length=60, verbose_name='Janr')

    def __str__(self):
        return f"{self.book_name}"

    class Meta:
        verbose_name = 'Kitab'
        verbose_name_plural = 'Kitab'
        ordering = ['book_name']


class Reader(models.Model):
    first_name = models.CharField(max_length=60, verbose_name='Ad')
    last_name = models.CharField(max_length=60, verbose_name='Soyad')
    document_id = models.SlugField(unique=True, verbose_name='FİN kod', max_length=7)
    id_number = models.PositiveIntegerField(unique=True, verbose_name='İd nömrəsi', default=get_number,
                                            null=True, blank=True)
    black_list = models.BooleanField(default=False, verbose_name='Qara siyahı', )
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Əlavə tarixi')

    def __str__(self):
        return f"{self.id_number}"

    class Meta:
        verbose_name = 'Oxuyucu'
        verbose_name_plural = 'Oxuyucu'
        ordering = ['first_name']


class GiveBook(models.Model):
    book_name = models.ForeignKey(Book, on_delete=models.PROTECT, verbose_name='Kitab adı')
    reader = models.ForeignKey(Reader, on_delete=models.PROTECT, related_name='reader_id', verbose_name='Oxuyucunun id nömrəsi')
    date_received = models.DateField(verbose_name='Götürdüyü tarix')
    will_return_date = models.DateField(verbose_name='Qataracağı tarix')

    def __str__(self):
        return f"{self.reader}"

    class Meta:
        verbose_name = 'İcarə'
        verbose_name_plural = 'İcarə'
        ordering = ['date_received']
