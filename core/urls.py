from django.urls import path
from . import views

urlpatterns = [
    path('details', views.student_details, name='index'),
]