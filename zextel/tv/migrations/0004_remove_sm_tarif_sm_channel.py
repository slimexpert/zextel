# Generated by Django 3.0.2 on 2020-06-13 20:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tv', '0003_sm_tarif'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sm_tarif',
            name='sm_channel',
        ),
    ]
