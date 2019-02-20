from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('process', views.process),
    path('show/<number>', views.show),
    path('success', views.index),
]
