# Generated by Django 2.1.5 on 2020-08-02 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20200802_1706'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ubication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]