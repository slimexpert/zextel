# Generated by Django 3.0.2 on 2020-03-14 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sl_title', models.CharField(max_length=100, verbose_name='Название слайдера')),
                ('sl_number', models.IntegerField(verbose_name='Очередность вывода слайдера')),
                ('sl_text', models.TextField(default='<div></div>', verbose_name='HTML сладера')),
                ('sl_show', models.BooleanField(default=1, verbose_name='Показывать слайдер')),
            ],
        ),
    ]
