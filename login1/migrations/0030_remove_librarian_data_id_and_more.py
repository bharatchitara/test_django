# Generated by Django 4.0.4 on 2022-05-26 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login1', '0029_remove_librarian_data_id_and_more'),
    ]

    operations = [
       
        migrations.AddField(
            model_name='book_history',
            name='submit_status',
            field=models.IntegerField(default=0),
        ),
       
    ]