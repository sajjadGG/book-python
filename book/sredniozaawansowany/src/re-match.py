import re

POPRAWNY_EMAIL = r'^[a-zA-Z0-9][\w.+-]*@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'


def email_poprawny(email):
    if re.match(POPRAWNY_EMAIL, email):
        print(f'Poprawny: {email}')
    else:
        print(f'Niepoprawny: {email}')


email_poprawny('matt@astrotech.io')  # Poprawny
email_poprawny('Matt@astrotech.io')  # Poprawny
email_poprawny('+matt@astrotech.io')  # Niepoprawny
email_poprawny('matt+@astrotech.io')  # Poprawny
email_poprawny('matt+facebook.com@astrotech.io')  # Niepoprawny
email_poprawny('matt@.io')  # Poprawny
