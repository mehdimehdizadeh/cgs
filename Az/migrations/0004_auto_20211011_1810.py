# Generated by Django 3.2.3 on 2021-10-11 14:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Az', '0003_team'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='about',
            name='image2',
        ),
        migrations.RemoveField(
            model_name='about',
            name='image3',
        ),
    ]
