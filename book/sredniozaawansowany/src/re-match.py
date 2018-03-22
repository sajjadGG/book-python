import re

POPRAWNY_EMAIL = r'(^[a-z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)'


def email_poprawny(email):
    if re.match(POPRAWNY_EMAIL, email):
        print('Poprawny:', email)
        return True
    else:
        print('Niepoprawny:', email)
        return False


email_poprawny('Amatt@astrotech.io')
email_poprawny('matt@astrotech.io')
email_poprawny('+matt@astrotech.io')
email_poprawny('matt+@astrotech.io')
email_poprawny('mattastrotech@.io')