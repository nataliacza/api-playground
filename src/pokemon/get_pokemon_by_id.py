from pprint import pprint

import requests


__pokemon_url = "https://pokeapi.co/api/v2/pokemon/"

def get_pokemon(poke_id: int):

    get_poke_url = f"{__pokemon_url}{poke_id}"
    response = requests.get(get_poke_url)

    return response


# pokemon_number = int(input("What is the Pokemon's ID? "))
pokemon_number = 50
action = get_pokemon(pokemon_number)
pprint(action.json())
