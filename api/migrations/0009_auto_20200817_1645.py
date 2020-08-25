# Generated by Django 2.1.5 on 2020-08-17 21:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20200816_1952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrada',
            name='UserPerchero',
            field=models.ForeignKey(blank=True, default=0, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.UserPerchero'),
        ),
        migrations.AlterField(
            model_name='perchado',
            name='ubication',
            field=models.ForeignKey(blank=True, default=0, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Ubication'),
        ),
        migrations.AlterField(
            model_name='salida',
            name='UserPerchero',
            field=models.ForeignKey(blank=True, default=0, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.UserPerchero'),
        ),
    ]