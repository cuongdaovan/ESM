from django.urls import path

from . import views

from rest_framework_simplejwt import views as jwt_view
from rest_framework import routers

router = routers.SimpleRouter()

urlpatterns = [
    path('api/v1/login/', views.LoginAPI.as_view(), name='login')
]
urlpatterns += router.urls
