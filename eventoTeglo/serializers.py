from rest_framework import serializers
from .models import Pesagem
from django.contrib.auth.models import User, Group


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('id','email','username')


class PesagemSerializer(serializers.HyperlinkedModelSerializer):
    #owner = serializers.ReadOnlyField(source='owner.usuario')

    class Meta:
        model = Pesagem
        fields = ('id','owner','peso')