from django.urls import path

from . import views

from rest_framework import routers

router = routers.DefaultRouter()
router.register('api/v1/modules', views.ModuleApi, basename='module')
router.register('api/v1/subjects', views.SubjectApi, basename='subject')
router.register('api/v1/faculties', views.FacultyApi, basename='faculty')

urlpatterns = [
    # path('subject/', school_view.SubjectList.as_view()),
]
urlpatterns += router.urls
