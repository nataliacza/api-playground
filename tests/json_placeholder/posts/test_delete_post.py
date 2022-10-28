from src.json_placeholder.posts.delete.delete_post import delete_post_id


def test_when_id_exists_returns_200():
    post_id = 1
    request = delete_post_id(post_id)

    assert request.status_code == 200


def test_when_invalid_id_type_provided_returns_400():
    post_id = "xxx"
    request = delete_post_id(post_id)

    assert request == 400
