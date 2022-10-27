import requests

from helpers.exceptions import ValidationException
from helpers.validators import user_exist, is_valid_int
from json_placeholder.my_dataclasses.posts import NewPost

json_url = "https://jsonplaceholder.typicode.com/posts"


print("==ADD NEW POST==")
input_title = input("Provide title: ")
input_body = input("Provide body: ")
input_userId = input("Provide userId: ")


if input_userId == "":
    raise ValidationException("Id must be provided.")


if is_valid_int(input_userId):
    check_user = user_exist(input_userId)

    if check_user:
        new_post_object = NewPost(input_title, input_body, int(input_userId))
        add_post = requests.post(url=json_url, data=new_post_object.__dict__)
        print(f"Post created: {add_post.json()}")
    else:
        print(f"UserId '{input_userId}' not found.")
else:
    print(f"Invalid userId provided.")
