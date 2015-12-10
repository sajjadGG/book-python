import regex

email = 'matt@mattagile.com'


def is_valid_email(email):
    if regex.is_valid_email(email):
        print('Email jest ok')
    else:
        print('Email nie jest ok')


# print('Modularyzacja.__name__ = ' + __name__)
is_valid_email(email)
