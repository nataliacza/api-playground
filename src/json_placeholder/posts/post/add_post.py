import requests

from src.helpers.exceptions import ValidationException
from src.helpers.validators import user_exist, is_valid_int
from src.json_placeholder.my_dataclasses.posts import NewPost


__posts_url = "https://jsonplaceholder.typicode.com/posts/"

def create_new_post(body: str, title: str, user_id: int):

    if user_id == "":
        raise ValidationException("Id must be provided.")

    if is_valid_int(str(user_id)):
        check_user = user_exist(str(user_id))

        if check_user:
            new_post_object = NewPost(title=title, body=body, userId=int(user_id))
            add_post = requests.post(url=__posts_url, data=new_post_object.__dict__)
            return add_post
        else:
            return requests.status_codes.codes["not_found"]
    else:
        return requests.codes["bad_request"]


print("==ADD NEW POST==")
# input_title = input("Provide title: ")
# input_body = input("Provide body: ")
# input_userId = int(input("Provide userId: "))
input_title = "testTitle"
input_body = "testBod"
input_userId = 10

request = create_new_post(title=input_title, body=input_body, user_id=input_userId)
print(request)
# print(request.json())

