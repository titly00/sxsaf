from django.contrib import admin
from django.urls import path
from .views import CarBrandView,CarDetailView

urlpatterns = [
    path('ini/', CarBrandView.as_view()),
    path('ini/<int:pk>', CarDetailView.as_view())
]
