# Generated by Django 4.0 on 2022-11-23 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_alter_car_vin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='vin',
            field=models.CharField(db_index=True, max_length=64, unique=True, verbose_name='Він'),
        ),
    ]
