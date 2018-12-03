from django.urls import path
from . import views

from rest_framework import routers

router = routers.DefaultRouter()
router.register('api/v1/assessments', views.AssessmentApi, basename='SjAssessment')

urlpatterns = [
    path('assessment/', views.AssessmentUpdate.as_view())
]
urlpatterns += router.urls