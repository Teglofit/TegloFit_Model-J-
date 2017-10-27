from django.shortcuts import render
from rest_framework import viewsets, generics
from .models import Pesagem
from django.contrib.auth.models import User, Group
from .serializers import UserSerializer, PesagemSerializer
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly

#...

class UserViewSet(viewsets.ModelViewSet):
    """
    Ponto final da API que permite que os usuários sejam visualizados ou editados.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

#######
class PesagemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Pesagem.objects.all()
    serializer_class = PesagemSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,)


class PesagemList(generics.ListAPIView):
    queryset = Pesagem.objects.all()
    serializer_class = PesagemSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PesagemDetail(generics.RetrieveAPIView):
    queryset = Pesagem.objects.all()
    serializer_class = PesagemSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    #Permissão
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)