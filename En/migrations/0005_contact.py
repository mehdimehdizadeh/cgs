# Generated by Django 3.2.3 on 2021-10-11 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('En', '0004_auto_20211011_1810'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=150, verbose_name='Phone')),
                ('mail', models.CharField(max_length=150, verbose_name='Email')),
                ('locate', models.CharField(max_length=150, verbose_name='Address')),
                ('location', models.CharField(max_length=150, verbose_name='Location')),
            ],
            options={
                'verbose_name': 'Contact',
                'verbose_name_plural': 'Contact',
            },
        ),
    ]