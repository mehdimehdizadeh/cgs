# Generated by Django 3.2.3 on 2021-10-11 11:14

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aboutus', ckeditor.fields.RichTextField(verbose_name='About')),
                ('mission', ckeditor.fields.RichTextField(verbose_name='Mission')),
            ],
            options={
                'verbose_name': 'About us',
                'verbose_name_plural': 'About us',
            },
        ),
    ]
