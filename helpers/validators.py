
def is_valid_int(data: str):
    try:
        isinstance(int(data), int)
        return True
    except ValueError:
        return False
