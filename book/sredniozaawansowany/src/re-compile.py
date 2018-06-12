import re


DATABASE = [
    'jose.jimenez@nasa.gov',
    'Jose.Jimenez@nasa.gov',
    '+jose.jimenez@nasa.gov',
    'jose.jimenez+@nasa.gov',
    'jose.jimenez+newsletter@nasa.gov',
    'jose.jimenez@.gov',
    '@nasa.gov',
    'jose.jimenez@nasa.g',
]

REGEX_VALID_EMAIL = r'^[a-zA-Z0-9][\w.+-]*@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]{2,}$'


# compiles at every loop iteration, and then matches
for email in DATABASE:
    re.match(REGEX_VALID_EMAIL, email)


# compiling before loop, hence matching only inside
valid_email = re.compile(REGEX_VALID_EMAIL)

for email in DATABASE:
    valid_email.match(email)

