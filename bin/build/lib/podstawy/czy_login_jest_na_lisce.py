#!/usr/bin/env python3


def czy_login_jest_na_liscie(login, lista, *args, **kwargs):
    """
    >>> czy_login_jest_na_liscie('xxx', [])
    False
    >>> czy_login_jest_na_liscie('xxx', [])
    False
    >>> czy_login_jest_na_liscie('xxx', ['yyy', 'aaaa', 'bbb'])
    False
    >>> czy_login_jest_na_liscie('xxx', ['xxx', 'aaa'])
    True
    """

    if login in lista:
        return True
    else:
        return False


czy_login_jest_na_liscie(login='xxx', lista=['xxx', 'aaa'])
czy_login_jest_na_liscie('xxx', ['xxx', 'aaa'])
