from django.contrib import admin
from django.conf.urls import url, include
from eventoTeglo.views import *
from rest_framework import routers, serializers, viewsets
from eventoTeglo import views
from rest_framework_jwt.views import obtain_jwt_token


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'peso', views.PesagemViewSet)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^api-token-auth/', obtain_jwt_token),
]


