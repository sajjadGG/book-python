"""
* Assignment: Dataclass DefineBasic DatabaseDump
* Complexity: medium
* Lines of code: 13 lines
* Time: 13 min

English:
    1. You received input data in JSON format from the API
       a. `str` fields: firstname, lastname, role, username, password, email,
       b. `datetime` fields: born, last_login,
       c. `bool` fields: is_active, is_staff, is_superuser,
       d. `list[dict]` field: user_permissions
    2. Using `dataclass` model data as class `User`
       a. Note, that fields order is important for tests to pass
    3. Do not create additional classes to represent `permission` filed,
       leave it as `list[dict]`
    4. Run doctests - all must succeed

Polish:
    1. Otrzymałeś z API dane wejściowe w formacie JSON
       a. pola `str`: firstname, lastname, role, username, password, email,
       b. pola `datetime`: born, last_login,
       c. pola `bool`: is_active, is_staff, is_superuser,
       d. pola `list[dict]`: user_permissions
    2. Wykorzystując `dataclass` zamodeluj dane za pomocą klasy `User`
       a. Zwróć uwagę, że kolejność pól ma znaczenie aby testy przechodziły
    3. Nie twórz dodatkowych klas do reprezentacji pola `permission`,
       niech zostanie jako `list[dict]`
    4. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isclass
    >>> from dataclasses import is_dataclass

    >>> assert isclass(User)
    >>> assert is_dataclass(User)

    >>> attributes = User.__dataclass_fields__.keys()
    >>> list(attributes)  # doctest: +NORMALIZE_WHITESPACE
    ['firstname', 'lastname', 'role', 'username', 'password', 'email', 'born',
     'last_login', 'is_active', 'is_staff', 'is_superuser', 'user_permissions']

    >>> result = [User(**user['fields']) for user in json.loads(DATA)]

    >>> result  # doctest: +NORMALIZE_WHITESPACE
    [User(firstname='Melissa', lastname='Lewis', role='commander', username='mlewis', password='pbkdf2_sha256$120000$gvEBNiCeTrYa0$5C+NiCeTrYsha1PHogqvXNiCeTrY0CRSLYYAA90=', email='melissa.lewis@nasa.gov', born='1995-07-15', last_login='1970-01-01T00:00:00.000+00:00', is_active=True, is_staff=True, is_superuser=False, user_permissions=[{'eclss': ['add', 'modify', 'view']}, {'communication': ['add', 'modify', 'view']}, {'medical': ['add', 'modify', 'view']}, {'science': ['add', 'modify', 'view']}]),
     User(firstname='Rick', lastname='Martinez', role='pilot', username='rmartinez', password='pbkdf2_sha256$120000$aXNiCeTrY$UfCJrBh/qhXohNiCeTrYH8nsdANiCeTrYnShs9M/c=', email='rick.martinez@ansa.gov', born='1996-01-21', last_login=None, is_active=True, is_staff=True, is_superuser=False, user_permissions=[{'communication': ['add', 'view']}, {'eclss': ['add', 'modify', 'view']}, {'science': ['add', 'modify', 'view']}]),
     User(firstname='Alex', lastname='Vogel', role='chemist', username='avogel', password='pbkdf2_sha256$120000$eUNiCeTrYHoh$X32NiCeTrYZOWFdBcVT1l3NiCeTrY4WJVhr+cKg=', email='alex.vogel@esa.int', born='1994-11-15', last_login=None, is_active=True, is_staff=True, is_superuser=False, user_permissions=[{'eclss': ['add', 'modify', 'view']}, {'communication': ['add', 'modify', 'view']}, {'medical': ['add', 'modify', 'view']}, {'science': ['add', 'modify', 'view']}]),
     User(firstname='Chris', lastname='Beck', role='crew-medical-officer', username='cbeck', password='pbkdf2_sha256$120000$3G0RNiCeTrYlaV1$mVb62WNiCeTrYQ9aYzTsSh74NiCeTrY2+c9/M=', email='chris.beck@nasa.gov', born='1999-08-02', last_login='1970-01-01T00:00:00.000+00:00', is_active=True, is_staff=True, is_superuser=False, user_permissions=[{'communication': ['add', 'view']}, {'medical': ['add', 'modify', 'view']}, {'science': ['add', 'modify', 'view']}]),
     User(firstname='Beth', lastname='Johansen', role='sysop', username='bjohansen', password='pbkdf2_sha256$120000$QmSNiCeTrYBv$Nt1jhVyacNiCeTrYSuKzJ//WdyjlNiCeTrYYZ3sB1r0g=', email='', born='2006-05-09', last_login=None, is_active=True, is_staff=True, is_superuser=False, user_permissions=[{'communication': ['add', 'view']}, {'science': ['add', 'modify', 'view']}]),
     User(firstname='Mark', lastname='Watney', role='botanist', username='mwatney', password='pbkdf2_sha256$120000$bxS4dNiCeTrY1n$Y8NiCeTrYRMa5bNJhTFjNiCeTrYp5swZni2RQbs=', email='', born='1994-10-12', last_login=None, is_active=True, is_staff=True, is_superuser=False, user_permissions=[{'communication': ['add', 'modify', 'view']}, {'science': ['add', 'modify', 'view']}])]
"""

import json
from dataclasses import dataclass
from datetime import date, datetime
from typing import Optional

DATA = ('[{"model":"authorization.user","pk":1,"fields":{"firstname":"Melissa"'
        ',"lastname":"Lewis","role":"commander","username":"mlewis","password"'
        ':"pbkdf2_sha256$120000$gvEBNiCeTrYa0$5C+NiCeTrYsha1PHogqvXNiCeTrY0CRS'
        'LYYAA90=","email":"melissa.lewis@nasa.gov","born":"1995-07-15","last_'
        'login":"1970-01-01T00:00:00.000+00:00","is_active":true,"is_staff":tr'
        'ue,"is_superuser":false,"user_permissions":[{"eclss":["add","modify",'
        '"view"]},{"communication":["add","modify","view"]},{"medical":["add",'
        '"modify","view"]},{"science":["add","modify","view"]}]}},{"model":"au'
        'thorization.user","pk":2,"fields":{"firstname":"Rick","lastname":"Mar'
        'tinez","role":"pilot","username":"rmartinez","password":"pbkdf2_sha25'
        '6$120000$aXNiCeTrY$UfCJrBh/qhXohNiCeTrYH8nsdANiCeTrYnShs9M/c=","born"'
        ':"1996-01-21","last_login":null,"email":"rick.martinez@ansa.gov","is_'
        'active":true,"is_staff":true,"is_superuser":false,"user_permissions":'
        '[{"communication":["add","view"]},{"eclss":["add","modify","view"]},{'
        '"science":["add","modify","view"]}]}},{"model":"authorization.user","'
        'pk":3,"fields":{"firstname":"Alex","lastname":"Vogel","role":"chemist'
        '","username":"avogel","password":"pbkdf2_sha256$120000$eUNiCeTrYHoh$X'
        '32NiCeTrYZOWFdBcVT1l3NiCeTrY4WJVhr+cKg=","email":"alex.vogel@esa.int"'
        ',"born":"1994-11-15","last_login":null,"is_active":true,"is_staff":tr'
        'ue,"is_superuser":false,"user_permissions":[{"eclss":["add","modify",'
        '"view"]},{"communication":["add","modify","view"]},{"medical":["add",'
        '"modify","view"]},{"science":["add","modify","view"]}]}},{"model":"au'
        'thorization.user","pk":4,"fields":{"firstname":"Chris","lastname":"Be'
        'ck","role":"crew-medical-officer","username":"cbeck","password":"pbkd'
        'f2_sha256$120000$3G0RNiCeTrYlaV1$mVb62WNiCeTrYQ9aYzTsSh74NiCeTrY2+c9/'
        'M=","email":"chris.beck@nasa.gov","born":"1999-08-02","last_login":"1'
        '970-01-01T00:00:00.000+00:00","is_active":true,"is_staff":true,"is_su'
        'peruser":false,"user_permissions":[{"communication":["add","view"]},{'
        '"medical":["add","modify","view"]},{"science":["add","modify","view"]'
        '}]}},{"model":"authorization.user","pk":5,"fields":{"firstname":"Beth'
        '","lastname":"Johansen","role":"sysop","username":"bjohansen","passwo'
        'rd":"pbkdf2_sha256$120000$QmSNiCeTrYBv$Nt1jhVyacNiCeTrYSuKzJ//WdyjlNi'
        'CeTrYYZ3sB1r0g=","email":"","born":"2006-05-09","last_login":null,"is'
        '_active":true,"is_staff":true,"is_superuser":false,"user_permissions"'
        ':[{"communication":["add","view"]},{"science":["add","modify","view"]'
        '}]}},{"model":"authorization.user","pk":6,"fields":{"firstname":"Mark'
        '","lastname":"Watney","role":"botanist","username":"mwatney","passwor'
        'd":"pbkdf2_sha256$120000$bxS4dNiCeTrY1n$Y8NiCeTrYRMa5bNJhTFjNiCeTrYp5'
        'swZni2RQbs=","email":"","born":"1994-10-12","last_login":null,"is_act'
        'ive":true,"is_staff":true,"is_superuser":false,"user_permissions":[{"'
        'communication":["add","modify","view"]},{"science":["add","modify","v'
        'iew"]}]}}]')

# class: Using `dataclass` model data as class `User`
class User:
    ...


# Solution
@dataclass
class User:
    firstname: str
    lastname: str
    role: str
    username: str
    password: str
    email: str
    born: date
    last_login: Optional[datetime]
    is_active: bool
    is_staff: bool
    is_superuser: bool
    user_permissions: list[dict]
