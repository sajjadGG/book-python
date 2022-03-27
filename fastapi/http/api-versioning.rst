HTTP API Versioning
===================
* Always version API
* Have stable API!
* Do not use plural in resources
* Use HTTP Statuses
* Use HTTP Methods


Version names
-------------
* Semantic versioning
* Django versioning


API deprecation
---------------
* Policy
* Darkening
* PendingDeprecation
* Deprecation


How to version API?
-------------------
.. csv-table:: How to version API?
    :header: "Example", "Description"

    "``https://example.com/api/v2/user/10``", "API version as a part of URL"
    "``https://example.com/user/10?api=v2``", "Version as a parameter to URL"
    "``https://api-v2.example.com``", "Subdomain"
    "``https://api.example.com/v2/``", "Subdomain+URL"
    "``X-API-VERSION: 2``", "Version as a custom header with ``X-...`` prefix"
    "``Accept: application/vnd.api.v2``", "API version as a custom vendor prefix for ``Accept`` header"
    "``Accept: application/vnd.api.v2;q=0.9,application/vnd.api.v1;q=0.8``", "API version negotiation with weights using ``Accept`` header"


Use Case
--------
.. code-block:: text

    X-API-VERSION: 1.0
    {"name": "Mark Watney"}

    X-API-VERSION: 2.0
    {"firstname": "Mark", "lastname": "Watney"}
