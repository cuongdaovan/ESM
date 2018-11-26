from django.urls import path
from . import views as school_view

urlpatterns = [
    path('subject/', school_view.SubjectList.as_view())
]