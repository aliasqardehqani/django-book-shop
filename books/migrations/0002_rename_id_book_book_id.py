# Generated by Django 4.1.5 on 2023-01-07 14:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='id',
            new_name='book_id',
        ),
    ]
