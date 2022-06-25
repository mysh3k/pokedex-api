from django.db import models
from django.utils import timezone


class Type(models.Model):
    typeName = models.CharField(max_length=16)
    def __str__(self):
        return f'{self.typeName}'

class Location(models.Model):
    location = models.CharField(max_length=32)
    encounterType = models.CharField(max_length=16)
    def __str__(self):
        return f'{self.location}, {self.encounterType}'

class EggGroup(models.Model):
    groupName = models.CharField(max_length=16)
    def __str__(self):
        return f'{self.groupName}'

class Pokemon(models.Model):
    pokemonIndex = models.IntegerField()
    pokemonName = models.CharField(max_length=32)
    pokemonEvolution = models.ForeignKey("self", null=True, on_delete=models.DO_NOTHING, related_name='evolution')
    pokemonPrevolution = models.ForeignKey("self", null=True, on_delete=models.DO_NOTHING, related_name='prevolution')
    pokemonType = models.ManyToManyField(Type)
    pokemonEggGroup = models.ManyToManyField(EggGroup)
    pokemonLocation = models.ManyToManyField(Location)

