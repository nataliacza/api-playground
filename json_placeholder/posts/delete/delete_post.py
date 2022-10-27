from pprint import pprint

import requests

from helpers.validators import is_valid_int

print("==DELETE POST==")
input_postId = input("Provide postId: ")

url = f"https://jsonplaceholder.typicode.com/posts/"


if is_valid_int(input_postId):
    delete_url = "".join([url, input_postId])
    request = requests.delete(url=delete_url)
    if request.status_code == 200:
        print("Success!")
    elif request.status_code == 404:                # For this api delete will never return other code than 200
        print(f"Not found: {request.status_code}")
    else:
        print(request.status_code)
else:
    print("Invalid id provided.")
