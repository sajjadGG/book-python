import re

VALID_EMAIL = r'^[a-zA-Z0-9][\w.+-]*@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]{2,}$'


def is_valid_email(email: str) -> bool:
    """
    Function check email address against Regular Expression

    >>> is_valid_email('jose.jimenez@nasa.gov')
    True
    >>> is_valid_email('Jose.Jimenez@nasa.gov')
    True
    >>> is_valid_email('+jose.jimenez@nasa.gov')
    False
    >>> is_valid_email('jose.jimenez+@nasa.gov')
    True
    >>> is_valid_email('jose.jimenez+newsletter@nasa.gov')
    True
    >>> is_valid_email('jose.jimenez@.gov')
    False
    >>> is_valid_email('@nasa.gov')
    False
    >>> is_valid_email('jose.jimenez@nasa.g')
    False
    """
    if re.match(VALID_EMAIL, email):
        return True
    else:
        return False
