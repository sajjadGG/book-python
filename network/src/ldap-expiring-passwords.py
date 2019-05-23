# !/usr/bin/env python3

from datetime import datetime, timedelta
from pprint import pprint
from ldap3 import Server, Connection, SEARCH_SCOPE_WHOLE_SUBTREE


LDAP_HOST = "127.0.0.1"
LDAP_PORT = 389
LDAP_USER = "myusername"
LDAP_PASS = "mypassword"


def search(filter, basedn='OU=Users,DC=local', attributes=('mail', 'pwdLastSet')):
    with Connection(Server(LDAP_HOST, port=LDAP_PORT), user=LDAP_USER, password=LDAP_PASS) as ldap:
        ldap.search(basedn, filter, SEARCH_SCOPE_WHOLE_SUBTREE, attributes=attributes)
        return [record['attributes'] for record in ldap.response]


def datetime_to_mstimestamp(dt):
    """
    Active Directory has different approach to create timestamp than Unix.
    Here's a function to convert the Unix timestamp to the AD one.

    >>> dt = datetime(2000, 1, 1, 0, 0)
    >>> datetime_to_mstimestamp(dt)
    125911548000000000
    """
    timestamp = int(dt.timestamp())
    magic_number = 116_444_736_000_000_000
    shift = 10_000_000
    return (timestamp*shift) + magic_number


def mstimestamp_to_datetime(mstimestamp):
    """
    Active Directory has different approach to create timestamp than Unix.
    Here's a function to convert AD timestamp to the Unix one.

    >>> ms_timestamp = 130567328471235643
    >>> mstimestamp_to_datetime(ms_timestamp)
    datetime.datetime(2014, 10, 2, 16, 14, 7, 123563)
    """
    magic_number = 11_644_473_600
    shift = 10_000_000
    timestamp = (mstimestamp/shift) - magic_number
    return datetime.fromtimestamp(timestamp)


def month_ago(date):
    """
    >>> dt = datetime(2000, 1, 31, 0, 0)
    >>> month_ago(dt)
    datetime.datetime(2000, 1, 1, 0, 0)
    """
    return date - timedelta(days=30)


if __name__ == "__main__":
    now = datetime.now()
    since = month_ago(now)
    older_than_month_ago = f"""
        (&
           (objectCategory=Person)
           (userAccountControl=512)
           (pwdLastSet<={datetime_to_mstimestamp(since)})
           (mail=*)
        )
    """

    for user in search(older_than_month_ago):
        pwd_last_set = int(user['pwdLastSet'][0])
        user['pwdLastSet'] = mstimestamp_to_datetime(pwd_last_set)
        pprint(user)
