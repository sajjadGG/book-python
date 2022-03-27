Docker
======


Requirements
------------
* ``requirements.txt``

Minimal Setup:

.. code-block:: text

    fastapi
    uvicorn

Full Stack:

.. code-block:: text

    fastapi
    pydantic
    pydantic[email]
    sqlalchemy
    uvicorn[standard]
    passlib[bcrypt]
    python-jose[cryptography]
    python-multipart


Official Image
--------------
* ``Dockerfile``

.. code-block:: Dockerfile

    FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9
    COPY . /app/


Custom Image
------------
* ``Dockerfile``
* ``requirements.txt``
* ``docker-compose.yaml``

.. code-block:: text

    fastapi==0.75.*
    uvicorn[standard]==0.17.*
    httpx==0.22.*
    pydantic==1.9.*

.. code-block:: Dockerfile

    FROM python:3.10

    COPY requirements.txt /tmp/requirements.txt
    RUN pip install --no-cache-dir --upgrade -r /tmp/requirements.txt

    COPY src /src
    WORKDIR /src
    CMD uvicorn main:app --host 0.0.0.0 --port 80

    HEALTHCHECK --start-period=10s --interval=60s --timeout=3s --retries=3 \
      CMD curl --fail http://localhost:80/healthcheck || exit 1

.. code-block:: yaml

    services:

      myapp:
        image: myusername/myapp:${VERSION:-latest}
        build: myusername/myapp
        command: uvicorn main:app --reload --host 0.0.0.0 --port 80
        volumes:
          - ./src:/src
          - ./tests:/tests

>>> from fastapi import FastAPI
>>> app = FastAPI()
>>>
>>>
>>> @app.get('/healthcheck', status_code=200)
... async def healthcheck() -> bool:
...     return True
