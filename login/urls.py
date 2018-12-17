from django.urls import path

from . import views

from rest_framework_simplejwt import views as jwt_view
from rest_framework import routers

router = routers.SimpleRouter()
router.register('api/v1/login', views.LoginAPI, basename='User')

urlpatterns = [

]
urlpatterns += router.urls
