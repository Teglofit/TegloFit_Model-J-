from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Pessoa(models.Model):
    usuario = models.ForeignKey(User, related_name='pessoa', on_delete=models.CASCADE, null=True)
    idade = models.IntegerField
    altura = models.FloatField


class Pesagem(models.Model):
    owner = models.ForeignKey('auth.User', related_name='usuario', on_delete=models.CASCADE, null=True)
    peso = models.FloatField('peso', max_length=6)
    dataEHoraDePesagem = models.DateTimeField('dataEHoraDePesagem', default=timezone.now)


