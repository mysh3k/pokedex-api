from django.shortcuts import render
from rest_framework import viewsets, permissions
from PokedexAPI.serializers import PokemonsSerializer, LocationsSerializer, EggGroupsSerializer, TypesSerializer
from .models import Pokemon, EggGroup, Type, Location
# Create your views here.


class PokedexViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all().order_by('pokemonIndex')
    serializer_class = PokemonsSerializer
    permission_classes = [permissions.IsAuthenticated]


class EggGroupsViewSet(viewsets.ModelViewSet):
    queryset = EggGroup.objects.all()
    serializer_class = EggGroupsSerializer
    permission_classes = [permissions.IsAuthenticated]


class TypesViewSet(viewsets.ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypesSerializer
    permission_classes = [permissions.IsAuthenticated]


class LocationsViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationsSerializer
    permission_classes = [permissions.IsAuthenticated]


