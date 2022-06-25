from rest_framework import serializers
from .models import Pokemon, Type, EggGroup, Location


class PokemonsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pokemon
        fields = ['pokemonName', 'pokemonEvolution', 'pokemonPrevolution', 'pokemonType', 'pokemonType', 'pokemonEggGroup', 'pokemonLocation']


class TypesSerializer(serializers.HyperlinkedModelSerializer):
    tag = PokemonsSerializer(read_only=True, many=True)
    class Meta:
        model = Type
        fields = ['typeName', 'pokemonName']


class EggGroupsSerializer(serializers.HyperlinkedModelSerializer):
    tag = PokemonsSerializer(read_only=True, many=True)
    class Meta:
        model = EggGroup
        fields = ['groupName', 'pokemonName']


class LocationsSerializer(serializers.HyperlinkedModelSerializer):
    tag = PokemonsSerializer(read_only=True, many=True)
    class Meta:
        model = Location
        fields = ['location', 'encounterType', 'pokemonName']
