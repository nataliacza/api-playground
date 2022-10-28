import requests

from src.helpers.validators import is_valid_int


__posts_url = "https://jsonplaceholder.typicode.com/posts/"

def delete_post_id(post_id: int):
    if is_valid_int(str(post_id)):
        delete_url = "".join([__posts_url, str(post_id)])
        request = requests.delete(url=delete_url)
        return request        # For this api delete will never return other code than 200
    else:
        return requests.codes["bad_request"]


print("==DELETE POST==")
# input_postId = int(input("Provide postId: "))
input_postId = 5

action = delete_post_id(input_postId)
print(action)
