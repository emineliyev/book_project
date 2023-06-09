# Generated by Django 4.1.7 on 2023-03-26 21:12

import books.signals
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=60, unique=True, verbose_name='Kitab adı')),
                ('author', models.CharField(max_length=60, verbose_name='Müəllif')),
                ('genre', models.CharField(max_length=60, verbose_name='Janr')),
            ],
            options={
                'verbose_name': 'Kitab',
                'verbose_name_plural': 'Kitab',
                'ordering': ['book_name'],
            },
        ),
        migrations.CreateModel(
            name='Reader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=60, verbose_name='Ad')),
                ('last_name', models.CharField(max_length=60, verbose_name='Soyad')),
                ('class_number', models.PositiveIntegerField(verbose_name='Sinif kodu')),
                ('id_number', models.PositiveIntegerField(blank=True, default=books.signals.get_number, null=True, unique=True, verbose_name='İd nömrəsi')),
                ('black_list', models.BooleanField(default=False, verbose_name='Qara siyahı')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Əlavə tarixi')),
            ],
            options={
                'verbose_name': 'Oxuyucu',
                'verbose_name_plural': 'Oxuyucu',
                'ordering': ['first_name'],
            },
        ),
        migrations.CreateModel(
            name='GiveBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_received', models.DateField(verbose_name='Götürdüyü tarix')),
                ('will_return_date', models.DateField(verbose_name='Qataracağı tarix')),
                ('book_name', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='books.book', verbose_name='Kitab adı')),
                ('reader', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='books.reader', verbose_name='Oxuyucunun id nömrəsi')),
            ],
            options={
                'verbose_name': 'İcarə',
                'verbose_name_plural': 'İcarə',
                'ordering': ['date_received'],
            },
        ),
    ]
