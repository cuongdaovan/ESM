from django.views import generic
from django.shortcuts import get_object_or_404

from . import models as school_model
from . import serializers

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework_simplejwt import serializers as jwt_s
from rest_framework import permissions
from rest_framework import authentication


class ModuleApi(viewsets.ViewSet):
    authentication_classes = (authentication.TokenAuthentication,)

    def list(self, request):
        queryset = school_model.Module.objects.all()
        serializer = serializers.ModuleSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = school_model.Module.objects.all()
        module = get_object_or_404(queryset, pk=pk)
        serializer = serializers.ModuleSerializer(module)
        return Response(serializer.data)


class CustomAuthenticated(permissions.IsAuthenticated):
    def has_permission(self, request, view):
        header = request.META.get('HTTP_AUTHORIZATION')
        token = header.split(' ')[1]
        data = {'token': token}
        print(token)
        valid_data = jwt_s.TokenVerifySerializer().validate(data)
        if valid_data == {}:
            return True
        else:
            return False


class SubjectApi(viewsets.ViewSet):
    permission_classes = (CustomAuthenticated,)

    def list(self, request):
        header = request.META.get('HTTP_AUTHORIZATION')
        token = header.split(' ')[1]
        data = {'refresh': token}
        access_token = jwt_s.TokenRefreshSerializer().validate(data)
        queryset = school_model.Subject.objects.all()
        serializer = serializers.SubjectSerializer(queryset, many=True)
        response = Response(serializer.data)
        response['access_token'] = access_token
        return response

    def retrieve(self, request, pk=None):
        header = request.META.get('HTTP_AUTHORIZATION')
        token = header.split(' ')[1]
        data = {'refresh': token}
        access_token = jwt_s.TokenRefreshSerializer().validate(data)
        queryset = school_model.Subject.objects.all()
        subject = get_object_or_404(queryset, pk=pk)
        serializer = serializers.SubjectSerializer(subject)
        response = Response(serializer.data)
        response['access_token'] = access_token
        return response


class FacultyApi(viewsets.ViewSet):

    def list(self, request):
        queryset = school_model.Faculty.objects.all()
        serializer = serializers.FacultySerializer(queryset, many=True)
        return Response(serializer.data)
