*************************
Regex pattern compilation
*************************


* ``re.compile()``


Without compilation
===================
.. code-block:: python
    :caption: Compiles at every loop iteration, and then matches
    :emphasize-lines: 15

    import re


    PATTERN = r'^[a-zA-Z0-9][\w.+-]*@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]{2,}$'
    INPUT = [
        'mark.watney@nasa.gov',
        'Mark.Watney@nasa.gov',
        '+mark.watney@nasa.gov',
        'mark.watney+@nasa.gov',
        'mark.watney+newsletter@nasa.gov',
        'mark.watney@.gov',
        '@nasa.gov',
        'mark.watney@nasa.g']

    for email in INPUT:
        re.match(PATTERN, email)


With compilation
================
.. code-block:: python
    :caption: Compiling before loop, hence matching only inside
    :emphasize-lines: 15

    import re


    PATTERN = re.compile(r'^[a-zA-Z0-9][\w.+-]*@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]{2,}$')
    INPUT = [
        'mark.watney@nasa.gov',
        'Mark.Watney@nasa.gov',
        '+mark.watney@nasa.gov',
        'mark.watney+@nasa.gov',
        'mark.watney+newsletter@nasa.gov',
        'mark.watney@.gov',
        '@nasa.gov',
        'mark.watney@nasa.g']

    for email in INPUT:
        PATTERN.match(email)
