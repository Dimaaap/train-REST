from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Car(models.Model):
    vin = models.CharField(verbose_name='Він', db_index=True, unique=True, max_length=64)
    color = models.CharField(verbose_name='Колір', max_length=64)
    brand = models.CharField(verbose_name='Бренд', max_length=64)
    CAR_TYPES = (
        (1, 'Седан'),
        (2, 'Хечбек'),
        (3, 'Універсал'),
        (4, 'Купе'),
    )
    car_type = models.IntegerField(verbose_name='Тим автомобіля', choices=CAR_TYPES)
    user = models.ForeignKey(User, verbose_name='Користувач', on_delete=models.CASCADE)

