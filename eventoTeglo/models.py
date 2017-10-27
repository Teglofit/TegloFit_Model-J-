from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Pesagem(models.Model):
    #usuario = models.ForeignKey(User)
    owner = models.ForeignKey('auth.User', related_name='usuario', on_delete=models.CASCADE, null=True)
    #owner = models.ForeignKey('auth.User', related_name='usuario', on_delete=models.CASCADE, )
    peso = models.FloatField('peso', max_length=6)
    dataEHoraDePesagem = models.DateTimeField('dataEHoraDePesagem', default=timezone.now)


