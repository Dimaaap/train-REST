# Generated by Django 4.1.3 on 2022-11-19 16:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vin', models.CharField(db_index=True, max_length=64, verbose_name='Vin')),
                ('color', models.CharField(max_length=64, verbose_name='Колір')),
                ('brand', models.CharField(max_length=64, verbose_name='Бренд')),
                ('car_type', models.IntegerField(choices=[(1, 'Седан'), (2, 'Хечбек'), (3, 'Універсал'), (4, 'Купе')], verbose_name='Тим автомобіля')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Користувач')),
            ],
        ),
    ]