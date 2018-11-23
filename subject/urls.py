from django.urls import path

from . import views

urlpatterns = [
    path('subject', views.SubjectList.as_view(), name='subject_list')
]
