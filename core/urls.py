from django.urls import path
from . import views

urlpatterns = [
    path('details', views.intern_details, name='index'),
]