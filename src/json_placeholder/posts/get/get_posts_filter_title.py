import json
from pprint import pprint

import requests

__posts_url = "https://jsonplaceholder.typicode.com/posts/"


def filter_posts_by_title(search_fraze: str):
    get_posts = requests.get(__posts_url)

    if get_posts.status_code == 200:
        result = get_posts.json()

        titles = [item for item in result if search_fraze in item["title"]]
        if len(titles) != 0:
            return titles
        return requests.codes["not_found"]


# find_title = input("Provide text to search in title: ")
find_title = "voluptates"
action = filter_posts_by_title(find_title)
pprint(action)
