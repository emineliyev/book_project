from django import forms
from books.models import Reader, Book, GiveBook


class CreateReaderForm(forms.ModelForm):
    class Meta:
        model = Reader
        fields = ('first_name', 'last_name', 'document_id', 'id_number', 'black_list')
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'document_id': forms.TextInput(attrs={'class': 'form-control'}),
            'id_number': forms.NumberInput(attrs={'class': 'form-control', 'disabled': True}),
        }


class CreateBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('book_name', 'author', 'genre')
        widgets = {
            'book_name': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'genre': forms.TextInput(attrs={'class': 'form-control'}),
        }


class DateInput(forms.DateInput):
    input_type = 'date'


class GiveBookForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['book_name'].empty_label = 'Kitab seçilməyib'
        self.fields['reader'].empty_label = 'Oxuyucu seçilməyib'

    class Meta:
        model = GiveBook
        fields = ('book_name', 'reader', 'date_received', 'will_return_date')
        widgets = {
            'book_name': forms.Select(attrs={'class': 'form-control'}),
            'reader': forms.Select(attrs={'class': 'form-control'}),
            'date_received': forms.DateInput(attrs={'class': 'form-control', 'type': "date"}),
            'will_return_date': forms.DateInput(attrs={'class': 'form-control', 'type': "date"}),

        }
