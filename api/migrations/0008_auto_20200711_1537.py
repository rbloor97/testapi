# Generated by Django 2.1.2 on 2020-07-11 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20200711_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='despacho',
            name='Factura',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
