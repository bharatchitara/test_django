# Generated by Django 3.0.5 on 2022-05-19 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login1', '0027_auto_20220517_2305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_authentication',
            name='password',
            field=models.CharField(default='', max_length=350),
        ),
    ]