# Generated by Django 4.0.4 on 2022-04-21 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login1', '0012_books_history'),
    ]

    operations = [
        migrations.CreateModel(
            name='book_history',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stu_username', models.CharField(max_length=50)),
                ('book1', models.TextField()),
                ('book1_allocatedon', models.DateField()),
            ],
        ),
    ]
