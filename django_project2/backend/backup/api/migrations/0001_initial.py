# Generated by Django 5.0.7 on 2024-07-18 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Showroom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('showroom_name', models.CharField(max_length=50)),
                ('showroom_email', models.EmailField(max_length=34)),
                ('showroom_location', models.CharField(max_length=56)),
                ('capacity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=255)),
                ('model', models.CharField(max_length=255)),
                ('year', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('color', models.CharField(max_length=50)),
                ('is_available', models.BooleanField(default=True)),
                ('showroom', models.ManyToManyField(related_name='cars', to='api.showroom')),
            ],
        ),
    ]
