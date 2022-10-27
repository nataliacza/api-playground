from pprint import pprint

import requests


url = "https://jsonplaceholder.typicode.com/comments"

post_ids = input("Provide ids to search? (ex. 2, 5, 7, 11): ")

input_list = post_ids.strip().replace(" ", "").split(",")

def build_query(data: list):
    result = "?"
    for i, v in enumerate(data):
        if i == len(data)-1:
            result += f"postId={v}"
        else:
            result += f"postId={v}&"
    return result

query = build_query(input_list)

request = requests.get(url+query)

if request.ok:
    result = request.json()
    print(f"Results: {len(result)}")
    pprint(result)
