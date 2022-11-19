from django.shortcuts import render
from rest_framework import generics

from .serializers import CarDetailSerializer, CarListSerializer
from .models import Car


class CarCreateView(generics.CreateAPIView):
    serializer_class = CarDetailSerializer


class CarListView(generics.ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarListSerializer


class CarDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CarDetailSerializer
    queryset = Car.objects.all()
