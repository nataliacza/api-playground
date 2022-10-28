from src.helpers.exceptions import ValidationException


def test_validation_exception_class_inheritance():
    initiate = ValidationException()
    assert isinstance(initiate, Exception)
