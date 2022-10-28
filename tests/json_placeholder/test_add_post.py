import pytest

from src.helpers.exceptions import ValidationException
from src.json_placeholder.posts.post.add_post import create_new_post


def test_when_userId_exists_returns_201():
    user_id = 1
    title = "testTitle"
    body = "testBody"
    response = create_new_post(user_id=user_id, title=title, body=body)

    assert response.status_code == 201
    assert response.json()["title"] == title
    assert response.json()["body"] == body
    assert response.json()["userId"] == str(user_id)


def test_when_user_id_does_not_exist_returns_404():
    user_id = 101
    title = "testTitle"
    body = "testBody"
    response = create_new_post(user_id=user_id, title=title, body=body)

    assert response == 404


def test_when_invalid_id_type_provided_returns_400():
    user_id = "xxx"
    title = "testTitle"
    body = "testBody"
    response = create_new_post(user_id=user_id, title=title, body=body)

    assert response == 400


def test_when_user_id_not_provided_raises_exception():
    user_id = ""
    title = "testTitle"
    body = "testBody"

    with pytest.raises(ValidationException):
        create_new_post(user_id=user_id, title=title, body=body)
