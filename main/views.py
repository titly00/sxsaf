from django.shortcuts import get_object_or_404
from rest_framework import generics, viewsets
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from .models import CarBrand, Book, Author, Car
from .serializers import CarBrandSerializer, AuthorSerializer, BookSerializer, CarSerializer


# Create your views here.


class CarBrandView(generics.ListCreateAPIView):
    queryset = CarBrand.objects.all()
    serializer_class = CarBrandSerializer


class CarDetailView(generics.RetrieveAPIView):
    queryset = CarBrand.objects.all()
    serializer_class = CarBrandSerializer


class BookCreateAPIView(CreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class GETBookCreateAPIView(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer





class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


    def list(self, request):
        queryset = Car.objects.all()
        serializer = CarSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        car = get_object_or_404(Car, pk=pk)
        serializer = CarSerializer(car)
        return Response(serializer.data)

    def create(self, request):
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def update(self, request, pk=None):
        car = get_object_or_404(Car, pk=pk)
        serializer = CarSerializer(car, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def partial_update(self, request, pk=None):
        car = get_object_or_404(Car, pk=pk)
        serializer = CarSerializer(car, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        car = get_object_or_404(Car, pk=pk)
        car.delete()
        return Response(status=204)

class CarModelViewSet(viewsets.ModelViewSet):
        queryset = Car.objects.all()
        serializer_class = CarSerializer
