SMTP
====


Send plaintext email
--------------------
.. literalinclude:: src/smtp-email-text.py
    :language: python
    :caption: Send plaintext email


Send email with attachments
---------------------------
.. literalinclude:: src/smtp-email-attachment.py
    :language: python
    :caption: Send email with attachments


Secured connection to the SMTP server
-------------------------------------
.. literalinclude:: src/smtp-ssl.py
    :language: python
    :caption: Secured connection to the SMTP server


Assignments
-----------
.. todo:: Convert assignments to literalinclude

Send email
^^^^^^^^^^
* Assignment: Send email
* Complexity: medium
* Lines of code: 20 lines
* Time: 21 min

English:
    TODO: English Translation
          Run doctests - all must succeed

Polish:
    1. Połącz się z serwerem podanym przez prowadzącego
    2. Wyślij wiadomość email na podany przez prowadzącego adres
    3. Do wiadomości załącz plik ``pep20.txt``, który będzie wynikiem polecenia ``import this`` :pep:`20` -- The Zen of Python
    4. Uruchom doctesty - wszystkie muszą się powieść
