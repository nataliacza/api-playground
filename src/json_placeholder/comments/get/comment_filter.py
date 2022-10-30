from pprint import pprint

import requests


__comments_url = "https://jsonplaceholder.typicode.com/comments"


def build_query(input_data: str):
    input_clean = input_data.strip().replace(" ", "").split(",")
    result_query = f"{__comments_url}?"
    for i, v in enumerate(input_clean):
        if i == len(input_clean)-1:
            result_query += f"postId={v}"
        else:
            result_query += f"postId={v}&"
    return result_query


def get_comments_by_post_id(input_data: str):
    if input_data != "":
        query = build_query(input_data)
        request = requests.get(query)

        if request.status_code == 200:
            return request
    else:
        request = requests.get(__comments_url)
        return request


# post_ids = input("Provide ids to search? (ex. 2, 5, 7, 11): ")
post_ids = "2, 5, 7, 11"
action = get_comments_by_post_id(post_ids)
pprint(action.json())
