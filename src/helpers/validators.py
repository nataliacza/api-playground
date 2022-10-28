import requests


def is_valid_int(data: str) -> bool:
    is_digit = data.strip().isdigit()
    if is_digit:
        if int(data) > 0:
            return True
    return False


def user_exist(user_id: str) -> bool:
    get_user_url = f"https://jsonplaceholder.typicode.com/users/{int(user_id)}"
    result = requests.get(get_user_url)
    if result.ok:
        return True
    else:
        return False
