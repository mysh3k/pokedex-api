from rest_framework import serializers
from .models import Pokemon, Type, EggGroup, Location


class PokemonsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pokemon
        fields = ['pokemonIndex', 'pokemonName', 'pokemonEvolution', 'pokemonPrevolution', 'pokemonType', 'pokemonEggGroup', 'pokemonLocation']

class PokemonsSerializer2(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pokemon
        fields = ['pokemonIndex', 'pokemonName', 'pokemonType', 'pokemonEggGroup', 'pokemonLocation']


class TypesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Type
        fields = ['typeName', 'type2']


class EggGroupsSerializer(serializers.HyperlinkedModelSerializer):
    tag = PokemonsSerializer(read_only=True, many=True)
    class Meta:
        model = EggGroup
        fields = ['groupName', 'tag']


class LocationsSerializer(serializers.HyperlinkedModelSerializer):
    tag = PokemonsSerializer(read_only=True, many=True)
    class Meta:
        model = Location
        fields = ['location', 'encounterType', 'tag']
