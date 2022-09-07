from enum import Enum
from django.db import models
from django.conf import settings
from django.utils import timezone
from mutagen.mp3 import MP3
from django.core.validators import FileExtensionValidator
# Create your models here.


# Create class for the right order by name request
class LowerCharField(models.CharField):
    def to_python(self, value):
        return value.lower()


GENRES = (
    ('rock', 'Rock'),
    ('acoustic/folk', 'Acoustic/Folk'),
    ('cinematic', 'Cinematic'),
    ('corporate/pop', 'Corporate/pop'),
    ('electronica', 'Electronica'),
    ('urban/groove', 'Urban/groove'),
    ('jazz', 'Jazz'),
    ('world/other', 'World/other')
)


class Song(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = LowerCharField(max_length=15)
    singer = models.CharField(max_length=15)
    upload = models.FileField(upload_to='', validators=[FileExtensionValidator(allowed_extensions=['mp3'])])
    # TODO: исползовать поле autonow_add  или что-то такое у DateTimeField (delete from form)
    # TODO: Добавить цикл for, кодировать слеш(url), добавить bootstrap, передавать жанр all, написать свой класс фильтр для обработки запроса
    #created_date = models.DateTimeField(auto_now_add=True)
    created_date = models.DateTimeField(default=timezone.now)
    duration = models.IntegerField(default=0)
    genre = models.CharField(
        max_length=32,
        choices=GENRES,
        default='rock',
    )

    def __str__(self):
        return self.name

    def get_duration(self):
        audio = MP3(self.upload.file)
        return int(audio.info.length)

    def save(self, *args, **kwargs):
        self.duration = self.get_duration()
        super(Song, self).save(*args, **kwargs)
