from src.json_placeholder.posts.get.get_posts_filter_title import filter_posts_by_title


def test_when_empty_string_provided_returns_list():
    fraze = ""
    response = filter_posts_by_title(fraze)

    assert response is not None
    assert isinstance(response, list) is True


def test_when_fraze_not_exist_returns_404():
    fraze = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    response = filter_posts_by_title(fraze)

    assert response == 404


def test_when_fraze_exist_returns_4_elements():
    fraze = "voluptates"
    response = filter_posts_by_title(fraze)

    assert len(response) == 4
