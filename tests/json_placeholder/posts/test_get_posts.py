from src.json_placeholder.posts.get.get_posts import get_all_posts


def test_when_no_limit_provided_returns_list():
    response = get_all_posts()

    assert response is not None
    assert len(response) == 100
    assert isinstance(response, list) is True


def test_when_limit_5_provided_returns_list_with_5_elements():
    limit_given = 5
    response = get_all_posts(limit_given)

    assert response is not None
    assert len(response) == 5


def test_when_invalid_limit_provided_returns_400():
    limit_given = "invalid"
    response = get_all_posts(limit_given)

    assert response == 400
