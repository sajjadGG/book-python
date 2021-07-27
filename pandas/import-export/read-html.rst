Pandas Read HTML
================


Rationale
---------
* File paths works also with URLs


Read HTML
---------
.. code-block:: python

    DATA = 'https://python.astrotech.io/numerical-analysis/pandas/df-create.html'

    pd.read_html(DATA)
    # Traceback (most recent call last):
    # urllib.error.HTTPError: HTTP Error 403: Forbidden

.. code-block:: python

    import requests

    DATA = 'https://python.astrotech.io/numerical-analysis/pandas/df-create.html'

    USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'

    resp = requests.get(DATA, headers={'User-Agent': USER_AGENT})
    dfs = pd.read_html(resp.content)

    dfs[0]
    #      Crew Role        Astronaut
    # 0   Prime  CDR   Neil Armstrong
    # 1   Prime  LMP      Buzz Aldrin
    # 2   Prime  CMP  Michael Collins
    # 3  Backup  CDR     James Lovell
    # 4  Backup  LMP   William Anders
    # 5  Backup  CMP       Fred Haise



Assignments
-----------
.. literalinclude:: assignments/pandas_read_html.py
    :caption: :download:`Solution <assignments/pandas_read_html.py>`
    :end-before: # Solution
