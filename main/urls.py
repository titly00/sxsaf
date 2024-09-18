
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CarBrandView, CarDetailView, BookCreateAPIView,GETBookCreateAPIView,CarModelViewSet

router = DefaultRouter()
router.register(r'cars',CarModelViewSet)
urlpatterns = [
    path('cars/', include(router.urls)),
    path('ini/', CarBrandView.as_view()),
    path('ini/<int:pk>', CarDetailView.as_view()),
    path('in/',BookCreateAPIView.as_view()),
    path('get/',GETBookCreateAPIView.as_view()),
    path('get/<int:pk>/', CarDetailView.as_view())
]
