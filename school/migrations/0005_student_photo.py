# Generated by Django 4.2.7 on 2023-12-13 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0004_student_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='photo',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
