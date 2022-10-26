
def is_valid_id(data: str):
    try:
        isinstance(int(data), int)
        return True
    except ValueError:
        return False
