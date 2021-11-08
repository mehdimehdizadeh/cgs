# Generated by Django 3.2.3 on 2021-10-14 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sosials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Sosial şəbəkənin adının ti kodu')),
                ('link', models.CharField(max_length=150, verbose_name='Sosial şəbəkənin adı')),
            ],
            options={
                'verbose_name': 'Sosial şəbəkə',
                'verbose_name_plural': 'Sosial şəbəkələr',
                'ordering': ['-id'],
            },
        ),
    ]