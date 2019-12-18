*****
Cache
*****

.. code-block:: python

    if os.path.exists('/tmp/memcached.sock'):
        CACHES = {
            'default': {
                'BACKEND': 'django.core.cache.backends.memcached.PyLibMCCache',
                'LOCATION': '/tmp/memcached.sock',

                # Use binary memcache protocol (needed for authentication)
                'BINARY': True,

                # TIMEOUT is not the connection timeout! It's the default expiration
                # timeout that should be applied to keys! Setting it to `None`
                # disables expiration.
                'TIMEOUT': None,

                'OPTIONS': {
                    # Enable faster IO
                    'tcp_nodelay': True,

                    # Keep connection alive
                    'tcp_keepalive': True,

                    # Timeout settings
                    'connect_timeout': 2000,  # ms
                    'send_timeout': 750 * 1000,  # us
                    'receive_timeout': 750 * 1000,  # us
                    '_poll_timeout': 2000,  # ms

                    # Better failover
                    'ketama': True,
                    'remove_failed': 1,
                    'retry_timeout': 2,
                    'dead_timeout': 30,
                }
            }
        }
    else:
        CACHES = {
            'default': {
                'BACKEND': 'django.core.cache.backends.dummy.DummyCache'
            }
        }