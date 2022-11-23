from rest_framework import serializers

from .models import Car


class CarDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Car
        fields = '__all__'


class CarListSerializer(serializers.ModelSerializer):
    # Поле,яке приховує поле з вибором користувача,який додав назву машини в базу даних,
    # метод автоматично додає в те поле значення користувача,який це робить,якщо він авторизований
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Car
        fields = '__all__'
