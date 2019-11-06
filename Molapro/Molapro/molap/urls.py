from django.urls import path
from molap import views

urlpatterns = [
    path ('', views.molap, name='molap')
]