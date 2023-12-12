import random

def generate_unique_password(digits=8):
    """
    This function will generate unique password with given digits.
    
    By default will generate 8 digit password.
    """
    digits = max(digits, 1)
    password = ''.join(str(random.randrange(10)) for _ in range(digits))

    return password