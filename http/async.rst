***********************
Asynchronous processing
***********************


``Celery``
==========
.. glossary::

    Celery
        A task queue implementation for *Python* web applications used to asynchronously execute work outside the *HTTP* request-response cycle. *Celery* can be used to run batch jobs in the background on a regular schedule.

Why?
----
* You want your *WSGI* server to respond to incoming requests as quickly as possible.
* Each request ties up a worker process until the response is finished.
* Moving work off those workers by spinning up asynchronous jobs as tasks in a queue is a straightforward way to improve *WSGI* server response times.

Celery daemon
-------------
* ``celeryd``
* Executes tasks
* Workers that handle whatever tasks you put
* Each worker will perform a task
* When the task is completed will pick up the next one
* The cycle will repeat continuously
* Waiting idly when there are no more tasks

Celerybeat
----------
* scheduler
* cron like
* example execution:

    - at time intervals (every 5 seconds or once a week),
    - on a specific date or time (at 5:03pm every Sunday)

Install
-------
* Requires ``RabbitMQ``

.. code-block:: console

    pip install celery

Basic usage
-----------
#. Define task in ``tasks.py`` file by decorating function

    .. code-block:: python
        :caption: tasks.py

        from celery import Celery

        app = Celery('tasks', broker='pyamqp://guest@localhost//')

        @app.task
        def add(x, y):
            return x + y

#. Run *Celery* workers with ``tasks`` module (use verbose "info" logging)

    .. code-block:: console

        celery -A tasks worker --loglevel=info

#. Call function asynchronously by using ``.delay()`` special method added by Celery

    .. code-block:: python

        from tasks import add

        result = add.delay(4, 4)

#. If you want to store results use:

    .. code-block:: python

        app = Celery('tasks', backend='db+sqlite:///results.sqlite', broker='amqp://')

#. Check status

    .. code-block:: python

        result.ready()
        # False

        result.failed()
        # False

        result.successful()
        # False

        result.state       # PENDING -> STARTED -> SUCCESS
        # 'PENDING'

More info
---------
* http://docs.celeryproject.org/en/latest/getting-started/first-steps-with-celery.html
* https://www.youtube.com/watch?v=68QWZU_gCDA
* https://www.youtube.com/watch?v=-ISgjBQDnhw


``RabbitMQ``
============
* *RabbitMQ* is the most widely deployed open source message broker
* Implementation of the *Advanced Message Queuing Protocol* (*AQMP*)
* *AQMP* is an open standard

.. glossary::

    Messaging
        A message is a way of exchanging information between application, servers and processes. When two applications share data among themselves, they can decide when to react to it when they receive the data. To exchange data effectively, one application should be independent of another application. This independence part is where a message broker comes in.

    Message Broker
        A message broker is an application which stores messages for an application. Whenever an application wants to send data to another application, the app publishes the message onto the message broker. The message broker then finds out which queue this message belongs to, finds out the apps which are connected to that queue and so, those apps can now consume that message.

        The message broker app, like *RabbitMQ*, is responsible for saving that message until there is a consumer for that message. Queues are just virtually infinite buffers which store message packets.

Install
-------
Using Docker:

    .. code-block:: console

        docker run -d -p 5462:5462 rabbitmq

Ubuntu or Debian package:

    .. code-block:: console

        echo "deb http://www.rabbitmq.com/debian/ testing main" >> /etc/apt/sources.list
        curl http://www.rabbitmq.com/rabbitmq-signing-key-public.asc | sudo apt-key add -
        sudo apt-get update
        sudo apt-get install -y rabbitmq-server

Config
------
.. code-block:: console

    vim /etc/default/rabbitmq-server

Management Console
------------------
* Manage users and their permissions and roles
* Create new queues
* Manage queues, monitor their consumption rate etc.
* Purge data which is currently on queues
* Send and receive messages
* Memory usage against each queue and by the overall process

.. code-block:: console

    sudo rabbitmq-plugins enable rabbitmq_management

.. code-block:: console

    open http://localhost:15672/

Default credentials is:

    - username: ``guest``
    - password: ``guest``

Change this:

    .. code-block:: console

        sudo rabbitmqctl add_user admin password
        sudo rabbitmqctl set_user_tags admin administrator
        sudo rabbitmqctl set_permissions -p / admin ".*" ".*" ".*"

Manage RabbitMQ
---------------
.. code-block:: console
    :caption: Start the service

    service rabbitmq-server start

.. code-block:: console
    :caption: Stop the service

    service rabbitmq-server stop

.. code-block:: console
    :caption: Restart the service

    service rabbitmq-server restart

.. code-block:: console
    :caption: Check the status

    service rabbitmq-server status
