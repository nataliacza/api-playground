from src.json_placeholder.posts.patch.patch_post import update_post_by_id


def test_when_id_exists_returns_200():
    post_id = 1
    title = "testTitle"
    body = "testBody"
    request = update_post_by_id(post_id, title, body)

    assert request.status_code == 200
    assert request.json()["id"] == post_id
    assert request.json()["title"] == title
    assert request.json()["body"] == body


def test_when_id_over_100_provided_returns_404():
    post_id = 101
    title = "testTitle"
    body = "testBody"
    request = update_post_by_id(post_id, title, body)

    assert request == 404


def test_when_invalid_id_type_provided_returns_400():
    post_id = "xxx"
    title = "testTitle"
    body = "testBody"
    request = update_post_by_id(post_id, title, body)

    assert request == 400
