from pprint import pprint

import requests

from src.helpers.validators import is_valid_int


__pokemon_url = "https://pokeapi.co/api/v2/pokemon/"


def get_pokemon(poke_id: str):

    if is_valid_int(poke_id):
        get_poke_url = f"{__pokemon_url}{int(poke_id)}"
        response = requests.get(get_poke_url)

        if response.ok:
            pokemon = response.json()
            return pokemon
    else:
        return None


def get_properties(selected_obj: dict, property_selected: str):
    if property_selected in selected_obj:
        return selected_obj[property_selected]
    else:
        return None


# Play with inputs
input_id = input("What is the Pokemon's ID? ")
response_pokemon = get_pokemon(input_id)

if response_pokemon is not None:
    print(f"You have selected id: {response_pokemon['id']}, name: {response_pokemon['name'].title()}\n")
    print(f"Available properties: {list(response_pokemon)}")
else:
    print("Invalid ID provided. Positive integer required.")


selected_property = input("Select property: ")
response_props = get_properties(response_pokemon, selected_property)

if response_props is not None:
    pprint(response_props)
else:
    print(f"'{selected_property}' property does not exist.")
