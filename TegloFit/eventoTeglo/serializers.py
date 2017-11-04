from rest_framework import serializers
from .models import Pessoa,Pesagem
from django.contrib.auth.models import User, Group


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id','email','username')


class PessoaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pessoa
        fields = ('id','altura','idade')


class PesagemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pesagem
        fields = ('id','owner','peso','dataEHoraDePesagem',)