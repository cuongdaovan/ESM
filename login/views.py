from django.shortcuts import render
from django.contrib.auth import views, authenticate
from django.contrib.auth import (
    login as auth_login,
    logout as auth_logout
)
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from rest_framework import status

from rest_framework_simplejwt import (
    serializers as jwt_s,
    views as jwt_v
)
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
from rest_framework.response import Response

from . import serializers
from .models import User as Login_user


class LoginView(views.LoginView):

    def form_valid(self, form):
        """Security check complete. Log the user in."""
        auth_login(self.request, form.get_user())
        token_r = jwt_s.TokenObtainPairSerializer.get_token(user=self.request.user)
        token_a = AccessToken().for_user(self.request.user)
        response = HttpResponseRedirect(self.get_success_url())
        response.set_cookie('refresh', token_r)
        response.set_cookie('access', token_a)
        return response


class LogoutView(views.LogoutView):
    def dispatch(self, request, *args, **kwargs):
        auth_logout(request)
        next_page = self.get_next_page()
        if next_page:
            # Redirect to this page until the session has been cleared.
            response = HttpResponseRedirect(
                'http://127.0.0.1:8080/api-auth/login/?next=%s' % next_page
            )
            response.set_cookie('access', ' ')
            response.set_cookie('refresh', ' ')
            return response
        return super().dispatch(request, *args, **kwargs)


class LoginAPI(jwt_v.TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        user = request.data
        username = user['username']
        password = user['password']
        user_auth = authenticate(request, username=username, password=password)
        if user_auth is not None:
            auth_login(request, user_auth)
            response = Response('success')
            access_token = AccessToken().for_user(user=user_auth)
            refresh_token = jwt_s.TokenObtainPairSerializer.get_token(user=user_auth)
            response['refresh_token'] = refresh_token
            response['access_token'] = access_token
            response.set_cookie('access_token', access_token)
            response.set_cookie('refresh_token', refresh_token)
            return response
        return Response('fail', status=status.HTTP_401_UNAUTHORIZED)
