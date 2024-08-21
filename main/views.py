from rest_framework import generics
from .models import CarBrand
from .serializers import CarBrandSerializer


# Create your views here.


class CarBrandView(generics.ListCreateAPIView):
    queryset = CarBrand.objects.all()
    serializer_class = CarBrandSerializer


class CarDetailView(generics.RetrieveAPIView):
    queryset = CarBrand.objects.all()
    serializer_class = CarBrandSerializer
