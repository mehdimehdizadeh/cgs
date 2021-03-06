# Generated by Django 3.2.3 on 2021-10-13 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Az', '0010_practice_practice_form'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='practice_form',
            options={'ordering': ['-id'], 'verbose_name': 'Təlimin form səhifəsi', 'verbose_name_plural': 'Təlimin form səhifəsi'},
        ),
        migrations.AddField(
            model_name='practice_form',
            name='practice',
            field=models.ManyToManyField(blank=True, to='Az.Practice', verbose_name='Təlimin növü'),
        ),
    ]
