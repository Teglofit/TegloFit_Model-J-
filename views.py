from django.shortcuts import render
from rest_framework import viewsets, generics
from .models import Pessoa,Pesagem
from django.contrib.auth.models import User, Group
from .serializers import UserSerializer, PessoaSerializer, PesagemSerializer
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly
#...

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PessoaViewSet(viewsets.ModelViewSet):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer


class PesagemViewSet(viewsets.ModelViewSet):
    queryset = Pesagem.objects.all()
    serializer_class = PesagemSerializer
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,)


