from pprint import pprint

import requests

from src.helpers.validators import is_valid_int


__posts_url = "https://jsonplaceholder.typicode.com/posts/"

def get_all_posts(items: int = None):
    posts = requests.get(__posts_url)

    if posts.ok:
        result_json = posts.json()

        if is_valid_int(str(items)):
            return result_json[:int(items)]
        elif items is None:
            return result_json
        return requests.codes["bad_request"]


# items_per_result = int(input("How many results to show? "))
items_per_result = 5

action = get_all_posts(items_per_result)
pprint(action)
