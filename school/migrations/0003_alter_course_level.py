# Generated by Django 4.2.7 on 2023-12-11 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_registration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='level',
            field=models.CharField(choices=[('B', 'Basic'), ('I', 'Intermediate'), ('A', 'Advanced')], default='B', max_length=1),
        ),
    ]