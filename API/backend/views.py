from django.shortcuts import render
from rest_framework import viewsets, filters
from .models import Pokemon
from .serializers import PokemonSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Q
import requests


#clase para obtener los primeros 50 pokemones de la api
class GetPokemon(APIView):
    #se sobreescribe el metodo get para obtener los primeros 50 pokemones de la api y mostrarlos en el navegador
    def get(self, request):
        for i in range(1,51):
            #se verifica si el pokemon ya existe en la base de datos para no volver a buscarlo en la api y guardarlo de nuevo
            if Pokemon.objects.filter(id=i).exists():
                print("El pokemon ya existe en la base de datos")
            else:
                #con la url de cada pokemon se obtiene la informacion de cada uno
                url = f'https://pokeapi.co/api/v2/pokemon/{i}'
                response = requests.get(url)
                if response.status_code == 200:
                    #se pasa la informacion a json y se guarda en la base de datos
                    data = response.json()
                    pokemon = Pokemon()
                    pokemon.id = data['id']
                    pokemon.name = data['name']
                    pokemon.type1 = data['types'][0]['type']['name']
                    if len(data['types']) > 1:
                        pokemon.type2 = data['types'][1]['type']['name']
                    pokemon.height = data['height']
                    pokemon.weight = data['weight']
                    pokemon.img_1 = data['sprites']['front_default']
                    pokemon.save()
                    print("Pokemon guardado: ", pokemon.name)
                else:
                    print("Error al guardar el pokemon, status code: ", response.status_code)
        queryset = Pokemon.objects.all()
        serializer = PokemonSerializer(queryset, many=True)
        return Response(serializer.data)
        



#clase para ver todos los pokemones que se encuentran en la base de datos para no usar GetPokemon cada vez que se quiera ver los pokemones
class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer

#clase para ver todos los Pokemon que pesen más de 30 y menos de 80
class PokemonWeightViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.filter(weight__gte=30, weight__lte=80)
    serializer_class = PokemonSerializer

# clase para ver todos los Pokemon tipo “grass”
class PokemonTypeViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.filter(Q(type1='grass')|Q(type2='grass'))
    serializer_class = PokemonSerializer
    

# clase para ver todos los Pokemon tipo “flying” que midan más de 10
class PokemonTypeHeightViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.filter(Q(type1='flying')|Q(type2='flying'),height__gte=10)
    serializer_class = PokemonSerializer
    


# clase para ver todos los nombres de los pokemones al revés
class PokemonNameViewSet(viewsets.ModelViewSet):

    queryset = Pokemon.objects.all()    
    serializer_class = PokemonSerializer

    # django viene con un metodo list que nos devuelve todos los objetos de la base de datos por defecto y para cambiarlo lo sobreescribimos
    # modificamos el metodo list para que nos devuelva los nombres al revés
    def list(self, request):
        queryset = Pokemon.objects.all()
        serializer = PokemonSerializer(queryset, many=True)
        for i in range(0, len(serializer.data)):
            serializer.data[i]['name'] = serializer.data[i]['name'][::-1]
        return Response(serializer.data)

#Clase para eliminar todos los pokemones de la base de datos
# (la tengo para probar el loading de la pagina)
class DeletePokemonsViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer

    def list(self, request):
        queryset = Pokemon.objects.all()
        queryset.delete()
        return Response("Pokemones eliminados")

