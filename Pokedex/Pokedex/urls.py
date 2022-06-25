from django.urls import include, path
from rest_framework import routers
from PokedexAPI import views

router = routers.DefaultRouter()

router.register(r'egggroups', views.EggGroupsViewSet)
router.register(r'types', views.TypesViewSet)
router.register(r'locations', views.LocationsViewSet)
router.register(r'pokedex', views.PokedexViewSet, basename='pokedex')
router.register(r'poketype', views.PokemonsOfTypeViewSet, basename='poketype')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]