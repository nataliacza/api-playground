from src.json_placeholder.comments.get.comment_filter import get_comments_by_post_id


def test_when_no_ids_provided_returns_all_comments():
    input_data = ""
    request = get_comments_by_post_id(input_data)

    assert request.status_code == 200
    assert len(request.json()) == 500


def test_when_one_post_id_provided_returns_5_results():
    input_data = "2"
    request = get_comments_by_post_id(input_data)

    assert request.status_code == 200
    assert len(request.json()) == 5


def test_when_non_existing_post_id_provided_returns_empty_list():
    input_data = "500"
    request = get_comments_by_post_id(input_data)

    assert request.status_code == 200
    assert len(request.json()) == 0
