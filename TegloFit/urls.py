"""TegloFit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.conf.urls import url, include
from eventoTeglo.views import *
from rest_framework import routers, serializers, viewsets
from eventoTeglo import views


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'peso', views.PesagemViewSet)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),

    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),

    url(r'^peso/$', views.PesagemList.as_view()),
    url(r'^peso/(?P<pk>[0-9]+)/$', views.PesagemDetail.as_view()),

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]


'''
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),

    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),

    url(r'^peso/$', views.PesagemList.as_view()),
    url(r'^peso/(?P<pk>[0-9]+)/$', views.PesagemDetail.as_view()),

    #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    
]
'''