# Generated by Django 2.1.5 on 2020-08-02 21:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20200802_1640'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perchado',
            name='nombre',
        ),
    ]
