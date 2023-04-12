from django.urls import path
from proyecto import views


urlpatterns = [
    path("", views.proyecto)
]
