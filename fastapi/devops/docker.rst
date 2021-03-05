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

    FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8-alpine3.10
    COPY . /app/


Custom Image
------------
* ``Dockerfile``

.. code-block:: Dockerfile

    FROM alpine
    COPY . /app
    WORKDIR /app
    EXPOSE 8000/tcp

    RUN apk add --no-cache python3 py3-pip \
     && pip install --no-cache-dir -r /app/requirements.txt

    CMD uvicorn main:app --host 0.0.0.0 --port 8000
