import pytest

from helpers.validators import is_valid_int


@pytest.mark.parametrize("input_data, expected_result", [
    ["example", False],
    ["5.5", False],
    ["2,4444", False],
    ["True", False],
    ["False", False],
    ["None", False]
])
def test_when_invalid_input_provided_returns_false(input_data, expected_result):
    result = is_valid_int(input_data)
    assert result is expected_result


@pytest.mark.parametrize("input_data, expected_result", [
    ["0", False],
    ["-1", False],
    ["-20", False],
    ["-1.55", False],
    ["-1,55", False],
])
def test_when_negative_number_or_zero_provided_returns_false(input_data, expected_result):
    result = is_valid_int(input_data)
    assert result is expected_result


@pytest.mark.parametrize("input_data, expected_result", [
    ["1", True],
    ["55", True],
])
def test_valid_positive_number_provided_returns_true(input_data, expected_result):
    result = is_valid_int(input_data)
    assert result is expected_result
