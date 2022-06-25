from django.shortcuts import render
from rest_framework import viewsets, permissions
from PokedexAPI.serializers import PokemonsSerializer, LocationsSerializer, EggGroupsSerializer, TypesSerializer
from .models import Pokemon, EggGroup, Type, Location
from rest_framework.decorators import authentication_classes, permission_classes
# Create your views here.


@authentication_classes([])
@permission_classes([])
class PokedexViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all().order_by('pokemonIndex')
    serializer_class = PokemonsSerializer
    permission_classes = [permissions.IsAuthenticated]


@authentication_classes([])
@permission_classes([])
class EggGroupsViewSet(viewsets.ModelViewSet):
    queryset = EggGroup.objects.all()
    serializer_class = EggGroupsSerializer
    permission_classes = [permissions.IsAuthenticated]


@authentication_classes([])
@permission_classes([])
class TypesViewSet(viewsets.ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypesSerializer
    permission_classes = [permissions.IsAuthenticated]


@authentication_classes([])
@permission_classes([])
class LocationsViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationsSerializer
    permission_classes = [permissions.IsAuthenticated]


