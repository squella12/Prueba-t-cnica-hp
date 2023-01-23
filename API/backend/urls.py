from django.urls import path, include
from rest_framework import routers
from .views import GetPokemon, PokemonViewSet, PokemonWeightViewSet, PokemonTypeViewSet, PokemonTypeHeightViewSet, PokemonNameViewSet, DeletePokemonsViewSet

router = routers.DefaultRouter()
router.register('pokemon', PokemonViewSet, basename='pokemon')
router.register('pokemonweight', PokemonWeightViewSet, basename='pokemonweight')
router.register('pokemontype', PokemonTypeViewSet, basename='pokemontype')
router.register('pokemontypeheight', PokemonTypeHeightViewSet, basename='pokemontypeheight')
router.register('pokemonname', PokemonNameViewSet, basename='pokemonname')
router.register('deletepokemon', DeletePokemonsViewSet, basename='deletepokemon')

urlpatterns = [
    path('getpokemon/', GetPokemon.as_view(), name='getpokemon'),
    
    
]
urlpatterns += router.urls
