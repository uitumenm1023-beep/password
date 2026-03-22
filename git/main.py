def is_valid_password(password):
    if len(password) < 6:
        return False
    if not any(c.isdigit() for c in password):
        return False
    if not any(c.isalpha() for c in password):
        return False
    return True

def is_valid_username(username):
    if len(username) < 3:
        return False
    if " " in username:
        return False
    return True