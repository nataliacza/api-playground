import requests

from src.helpers.validators import is_valid_int
from src.json_placeholder.my_dataclasses.posts import PatchPost


__posts_url = "https://jsonplaceholder.typicode.com/posts/"

def update_post_by_id(post_id: int, title: str, body: str):
    if is_valid_int(str(post_id)):

        # In db there are 100 posts - for non-existing ID response will be also code 200
        if int(post_id) > 100:
            return requests.status_codes.codes["not_found"]

        update_url = "".join([__posts_url, str(post_id)])
        update_data = PatchPost(title=title, body=body)
        action = requests.patch(url=update_url, data=update_data.__dict__)
        if action.ok:
            return action

    else:
        return requests.codes["bad_request"]

print("==PATCH POST==")
# input_postId = int(input("Provide postId: "))
# input_title = input("Provide title: ")
# input_body = input("Provide body: ")
input_postId = 5
input_title = "test"
input_body = "test"

result = update_post_by_id(post_id=input_postId, title=input_title, body=input_body)
print(result)
# print(result.json())
