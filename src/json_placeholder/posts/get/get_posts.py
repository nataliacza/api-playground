from pprint import pprint

import requests

from src.helpers.validators import is_valid_int

json_url = "https://jsonplaceholder.typicode.com/posts"

get_posts = requests.get(json_url)

if get_posts.ok:
    result_json = get_posts.json()

    items_per_result = input("How many results to show? ")

    if is_valid_int(items_per_result):
        pprint(result_json[:int(items_per_result)])
    else:
        print("Invalid input provided.")

    print("\n")
    user_id_input = input("Provide user id: ")

    if is_valid_int(user_id_input):
        user_posts = [item for item in result_json if item["userId"] == int(user_id_input)]
        print(f"Results: {len(user_posts)} of {len(result_json)}")
        pprint(user_posts)
    else:
        print("Invalid input provided.")

else:
    print("Unable to get data from requested source.")
