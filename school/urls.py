from django.urls import path
from . import views as school_view

from . import views

from rest_framework import routers

router = routers.DefaultRouter()
router.register('api/v1/modules', views.ModuleAPI, basename='module')

urlpatterns = [
    path('subject/', school_view.SubjectList.as_view()),
]
urlpatterns += router.urls
