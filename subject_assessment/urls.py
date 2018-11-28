from django.urls import path
from . import views
urlpatterns = [
    path('assessment/', views.AssessmentUpdate.as_view())
]