# Generated by Django 3.2.3 on 2021-10-17 13:06

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_adminadmin'),
    ]

    operations = [
        migrations.CreateModel(
            name='index_about',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Başlıq')),
                ('content', ckeditor.fields.RichTextField(verbose_name='Haqqında')),
            ],
        ),
    ]