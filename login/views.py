from django.shortcuts import render
from django.contrib.auth import views
from django.contrib.auth import (
    login as auth_login,
)
from django.http import HttpResponseRedirect

from rest_framework_simplejwt import serializers as jwt_s
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken


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
