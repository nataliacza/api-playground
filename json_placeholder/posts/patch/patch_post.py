from pprint import pprint

import requests

from helpers.validators import is_valid_int
from json_placeholder.my_dataclasses.posts import PatchPost

print("==PATCH POST==")
input_postId = input("Provide postId: ")
input_title = input("Provide title: ")
input_body = input("Provide body: ")

url = f"https://jsonplaceholder.typicode.com/posts/"


if is_valid_int(input_postId):
    update_url = "".join([url, input_postId])
    update_data = PatchPost(title=input_title, body=input_body)
    request = requests.patch(url=update_url, data=update_data.__dict__)
    if request.status_code == 200:
        pprint(request.json())
else:
    print("Invalid id provided.")
