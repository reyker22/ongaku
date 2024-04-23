from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models

from main.models import MyMusic


class User(AbstractUser):
    photo = models.ImageField(upload_to='users/%Y/%m/%d/', default=None, blank=True, null=True,
                              verbose_name='Фотография')
    phone = models.CharField(max_length=15, verbose_name='Телефон')

    my_music = models.ForeignKey(MyMusic, on_delete=models.CASCADE, blank=True, null=True,
                                 related_name='my_music', verbose_name='Моя музыка')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username


class Subscription(models.Model):
    start_date = models.DateField('Начало подписки')
    end_date = models.DateField('Конец подписки')
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, verbose_name='Пользователь')

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'

    def __str__(self):
        return self.user