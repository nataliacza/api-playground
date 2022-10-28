import requests
from pprint import pprint

from src.helpers.validators import is_valid_int

pokemon_number = input("What is the Pokemon's ID? ")

if is_valid_int(pokemon_number):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_number}"
    response = requests.get(url)

    if response.ok:
        pokemon = response.json()

        print(f"You have selected pokemon ID: {pokemon.get('id')}, name: {pokemon.get('name').title()}.")

        print(f"Available properties to get: {list(pokemon)}.")
        get_property = input("Select property: ")

        if pokemon.get(get_property) is not None:
            pprint(pokemon[get_property])
        else:
            print(f"'{get_property}' property does not exist.")
    else:
        print(f"Id '{pokemon_number}' does not exist.")

else:
    print("Invalid ID provided. Positive integer required.")
