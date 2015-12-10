import re


def is_valid_email(email):
    """
    >>> is_valid_email('matt+sages.com.pl@mattagile.com')
    True
    >>> is_valid_email('matt1234@mattagile.xxx')
    True
    >>> is_valid_email('hej@xxx')
    False
    >>> is_valid_email('hej')
    False
    """
    EMAIL_REGEX = re.compile(r'[a-zA-Z0-9._+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,3}')
    # print('Regexp.__name__ = ' + __name__)
    try:
        EMAIL_REGEX.match(email).group()
        return True
    except AttributeError:
        return False


def sprwadzie_ciagow():
    REGEX_IMIE_I_NAZWISKO = r"(?P<first_name>\w+) (?P<last_name>\w+)"
    imie_i_nazwisko = re.compile(REGEX_IMIE_I_NAZWISKO)
    m = imie_i_nazwisko.match('Malcolm Reynolds')

    m.group('first_name')
    'Malcolm'
    m.group('last_name')
    'Reynolds'
    m.group()
    'Malcolm Reynolds'


print('jestem zly')

if __name__ == '__main__':
    print('jestem dobry')
    is_valid_email('matt@mattagile.com')
    # sprwadzie_ciagow()
