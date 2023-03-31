from django.contrib import admin

from .models import Reader, Book, GiveBook


class ReaderAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'id_number', 'black_list')


admin.site.register(Reader, ReaderAdmin)
admin.site.register(Book)
admin.site.register(GiveBook)
