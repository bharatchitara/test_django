# Generated by Django 3.0.5 on 2022-05-13 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login1', '0020_alter_student_data_book1_alter_student_data_book2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_authentication',
            name='last_login',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
