# Generated by Django 4.2.2 on 2024-07-17 12:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_librarians_library'),
    ]

    operations = [
        migrations.RenameField(
            model_name='librarians',
            old_name='library',
            new_name='library_con',
        ),
    ]
