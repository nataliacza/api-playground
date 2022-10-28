import requests

from src.helpers.validators import is_valid_int


__pokemon_url = "https://pokeapi.co/api/v2/pokemon/"

def get_pokemon(poke_id: str):

    if is_valid_int(pokemon_number):
        get_poke_url = f"{__pokemon_url}{int(poke_id)}"
        response = requests.get(get_poke_url)

        if response.ok:
            pokemon = response.json()

            print(f"You have selected pokemon ID: {pokemon.get('id')}, name: {pokemon.get('name').title()}.\n")

        else:
            print(f"Id '{poke_id}' does not exist.")

    else:
        print("Invalid ID provided. Positive integer required.")


pokemon_number = input("What is the Pokemon's ID? ")

get_pokemon(pokemon_number)
