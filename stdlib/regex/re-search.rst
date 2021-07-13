RE Search
=========


Rationale
---------
* ``re.search()``
* Searches if pattern contains a string


Example
-------
* Usage of ``re.search()``

.. code-block:: python

    import re


    def contains(pattern, text)
        if re.search(pattern, text):
            return True
        else:
            return False


    COMMIT_MESSAGE = 'MYPROJ-1337, MYPROJ-997 removed obsolete comments'
    JIRA_ISSUEKEY = r'[A-Z]{2,10}-[0-9]{1,6}'
    REDMINE_NUMBER = r'#[0-9]+'

    contains(JIRA_ISSUEKEY, COMMIT_MESSAGE)      # True
    contains(REDMINE_NUMBER, COMMIT_MESSAGE)     # False


result = re.search('Neil Armstrong', DATA)
result.span()
(78, 92)
result.regs
((78, 92),)
DATA[78]
'N'
DATA[78:92]
'Neil Armstrong'



result = re.search('Mark Watney', DATA)
result.group()
AttributeError: 'NoneType' object has no attribute 'group'



result = re.search('Mark Watney', DATA)
if result:
    result.group()


if result := re.search('Mark Watney', DATA):
    result.group()


Assignments
-----------
.. literalinclude:: assignments/re_search_a.py
    :caption: :download:`Solution <assignments/re_search_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/re_search_b.py
    :caption: :download:`Solution <assignments/re_search_b.py>`
    :end-before: # Solution

.. literalinclude:: assignments/re_search_c.py
    :caption: :download:`Solution <assignments/re_search_c.py>`
    :end-before: # Solution

.. literalinclude:: assignments/re_search_d.py
    :caption: :download:`Solution <assignments/re_search_d.py>`
    :end-before: # Solution
