# Generated by Django 4.0.4 on 2022-04-19 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login1', '0007_student_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_data',
            name='username',
            field=models.CharField(default='101', max_length=50, primary_key=True, serialize=False),
        ),
    ]
