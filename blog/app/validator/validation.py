import re

def validate_email(email: str) -> bool:
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(pattern, email))

def validate_password(password: str) -> bool:
    return len(password) < 6

def validate_login(login: str) -> bool:
    if len(login) < 3 or len(login) > 20:
        return False
    pattern = r'^[a-zA-Z0-9_]+$'
    bool(re.match(pattern, login))

def validate_post_title(title: str) -> bool:
    return 1 <= len(title) <= 50


def validate_post_content(content: str) -> bool:
    return 1 <= len(content) <= 200