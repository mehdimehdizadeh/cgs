# Generated by Django 3.2.3 on 2021-10-14 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Az', '0015_vacancy'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancy',
            name='email',
            field=models.CharField(blank=True, max_length=150, verbose_name='Email'),
        ),
    ]
