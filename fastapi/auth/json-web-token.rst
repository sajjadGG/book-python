Auth JSON Web Token
===================
* JWT tokens


Install
-------
.. code-block:: console

    $ pip install 'python-jose[cryptography]' python-multipart


Using
-----
.. code-block:: console

    $ openssl rand -hex 32
    8dd0c72c203f1c63bd67d2089b9f3dd069873ef78688cf840c71a2237ec01d1f

Copy the output to the variable ``SECRET_KEY`` (don't use the one in the
example).

>>> SECRET_KEY = '8dd0c72c203f1c63bd67d2089b9f3dd069873ef78688cf840c71a2237ec01d1f'

Create a variable ``ALGORITHM`` with the algorithm used to sign the JWT
token and set it to ``"HS256"``.

>>> ALGORITHM = 'HS256'

Create a variable for the expiration of the token.

>>> ACCESS_TOKEN_EXPIRE_MINUTES = 30


Verify
------
.. code-block:: console

    $ curl -X GET http://localhost:8000/blog
    {"detail":"Not authenticated"}

    $ curl -X GET http://localhost:8000/login
    {"detail":"Method Not Allowed"}

    $ curl -X POST http://localhost:8000/login -d 'username=admin&password=admin'
    {"detail":"Invalid credentials"}

    $ curl -X POST http://localhost:8000/login -d 'username=mwatney&password=MyVoiceIsMyPassword'
    {"access_token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJtd2F0bmV5IiwiZXhwIjoxNjE0MTM1MDE4fQ.bbbXexg1lOLENxb-gAoU5xGLrk_VdcB4Aw9_cezEN0w","token_type":"bearer"}

    $ curl -X GET http://localhost:8000/blog
    {"detail":"Not authenticated"}

    $ curl -X GET http://localhost:8000/blog -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJtd2F0bmV5IiwiZXhwIjoxNjE0MTM1MDE4fQ.bbbXexg1lOLENxb-gAoU5xGLrk_VdcB4Aw9_cezEN0w'
    [{"title":"My Title","body":"My Content","published":true,"creator":{"username":"mwatney","email":"mwatney@nasa.gov"}}]
