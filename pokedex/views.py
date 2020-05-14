from django.http import HttpResponse
from django.template import loader

from .methods import check_database
from .models import Pokemon


def pokedex(request):
    check_database()
    pokemon_list = Pokemon.objects.all()
    template = loader.get_template('dex.html')
    context = {
        'title': 'Entire National Dex',
        'pokemons': pokemon_list,
    }
    return HttpResponse(template.render(context, request))


def pokemon(request, pokemon):
    pokemon = Pokemon.objects.filter(name=pokemon).first() or Pokemon.objects.filter(id=pokemon).first()
    template = loader.get_template('pokemon.html')
    context = {
        'title': pokemon,
        'pokemon': pokemon,
    }
    return HttpResponse(template.render(context, request))
