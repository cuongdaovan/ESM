from django.urls import path
from . import views as school_view

from . import views

from rest_framework import routers

# router = routers.SimpleRouter()


urlpatterns = [
    path('subject/', school_view.SubjectList.as_view()),
    path('api/v1/modules/', views.ModuleAPI.as_view())
]
