# Generated by Django 4.0.4 on 2022-04-27 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_admin', '0002_book_deleted'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('book', models.ManyToManyField(to='library_admin.book')),
            ],
        ),
    ]
