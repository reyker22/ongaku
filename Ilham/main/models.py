from django.contrib.auth import get_user_model
from django.db import models


class Album(models.Model):
    album_name = models.CharField(max_length=20, verbose_name='Название альбома')
    release_year = models.CharField(max_length=4, verbose_name='Год выпуска')
    genre = models.CharField(max_length=20, verbose_name='Жанр')

    class Meta:
        verbose_name = 'Альбом'
        verbose_name_plural = 'Альбомы'

    def __str__(self):
        return self.album_name


class Performers(models.Model):
    performer_name = models.CharField(max_length=30, verbose_name='Композитор')
    performer_img = models.ImageField(upload_to='tracks/performers/photo', default=None, blank=True, null=True,
                                      verbose_name='Фото композитора')

    class Meta:
        verbose_name = 'Композитор'
        verbose_name_plural = 'Композиторы'

    def __str__(self):
        return self.performer_name


class TrackList(models.Model):
    track_name = models.CharField(max_length=30, verbose_name='Название трека')
    track_img = models.ImageField(upload_to='tracks/albums/photo', default=None, blank=True, null=True,
                                  verbose_name='Фото альбома')
    genre = models.CharField(max_length=20, verbose_name='Жанр')
    duration = models.CharField(max_length=10, verbose_name='Длительность')
    album_id = models.ForeignKey('Album', on_delete=models.CASCADE, verbose_name='Альбом')
    performer = models.ForeignKey('Performers', on_delete=models.CASCADE, verbose_name='Композитор')

    class Meta:
        verbose_name = 'Трек лист'
        verbose_name_plural = 'Трек листы'

    def __str__(self):
        return self.track_name


class MyMusic(models.Model):
    music = models.ForeignKey('TrackList', on_delete=models.CASCADE, verbose_name='Музыка')

    class Meta:
        verbose_name = 'Моя музыка'
        verbose_name_plural = 'Мои музыки'

    def __str__(self):
        return self.music
