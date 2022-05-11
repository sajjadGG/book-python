Syntax Quantifier
=================
* Quantifier specifies how many occurrences of preceding qualifier or identifier
* Exact
* Greedy
* Lazy

>>> import re
>>> TEXT = 'Yuri Gagarin launched to space on Apr 12th, 1961 at 6:07 am.'
>>>
>>>
>>> re.findall(r'\d', TEXT)
['1', '2', '1', '9', '6', '1', '6', '0', '7']
>>>
>>> re.findall(r'\d\d\d\d', TEXT)
['1961']


Exact
-----
* Exact match
* ``{n}`` - exactly `n` repetitions, prefer longer

>>> import re
>>>
>>>
>>> TEXT = 'Yuri Gagarin launched to space on Apr 12th, 1961 at 6:07 am.'
>>>
>>> re.findall(r'[0-9]{2}', TEXT)
['12', '19', '61', '07']
>>>
>>> re.findall(r'\d{2}', TEXT)
['12', '19', '61', '07']


Greedy
------
* Prefer longest matches
* Default behavior
* ``{,n}`` - maximum `n` repetitions, prefer longer
* ``{n,}`` - minimum `n` repetitions, prefer longer
* ``{n,m}`` - minimum `n` repetitions, maximum `m` times, prefer longer
* ``*`` - minimum 0 repetitions, no maximum, prefer longer (alias to ``{0,}``)
* ``+`` - minimum 1 repetitions, no maximum, prefer longer (alias to ``{1,}``)
* ``?`` - minimum 0 repetitions, maximum 1 repetitions, prefer longer  (alias to ``{0,1}``)

>>> import re
>>>
>>>
>>> TEXT = 'Yuri Gagarin launched to space on Apr 12th, 1961 at 6:07 am.'
>>>
>>> re.findall(r'\d{2,4}', TEXT)
['12', '1961', '07']


Lazy
----
* Prefer shortest matches
* Non-greedy
* ``{,n}?`` - maximum `n` repetitions, prefer shorter
* ``{n,}?`` - minimum `n` repetitions, prefer shorter
* ``{n,m}?`` - minimum `n` repetitions, maximum `m` times, prefer shorter
* ``*?`` - minimum 0 repetitions, no maximum, prefer shorter (alias to ``{0,}?``)
* ``+?`` - minimum 1 repetitions, no maximum, prefer shorter (alias to ``{1,}?``)
* ``??`` - minimum 0 repetitions, maximum 1 repetition, prefer shorter (alias to ``{0,1}?``)

>>> import re
>>>
>>>
>>> TEXT = 'Yuri Gagarin launched to space on Apr 12th, 1961 at 6:07 am.'
>>>
>>> re.findall(r'\d{2,4}?', TEXT)
['12', '19', '61', '07']


Greedy vs. Lazy
---------------
>>> import re
>>>
>>>
>>> TEXT = 'Yuri Gagarin launched to space on Apr 12th, 1961 at 6:07 am.'
>>>
>>> re.findall(r'\d{2,4}', TEXT)  # Greedy
['12', '1961', '07']
>>>
>>> re.findall(r'\d{2,4}?', TEXT)  # Lazy
['12', '19', '61', '07']

Greedy vs Lazy in exact match has no difference:

>>> import re
>>>
>>>
>>> TEXT = 'Yuri Gagarin launched to space on Apr 12th, 1961 at 6:07 am.'
>>>
>>> re.findall('\d{2}?', TEXT)
['12', '19', '61', '07']
>>>
>>> re.findall('\d{2}', TEXT)
['12', '19', '61', '07']


Special
-------
>>> import re
>>>
>>>
>>> TEXT = 'Yuri Gagarin launched to space on Apr 12th, 1961 at 6:07 am.'
>>>
>>> re.findall('\d{0,}', TEXT) == re.findall('\d*', TEXT)
True
>>>
>>> re.findall('\d{1,}', TEXT) == re.findall('\d+', TEXT)
True

>>> import re
>>>
>>>
>>> TEXT = 'Yuri Gagarin launched to space on Apr 12th, 1961 at 6:07 am.'
>>>
>>> re.findall('\d+', TEXT)
['12', '1961', '6', '07']
>>>
>>> re.findall('\d*', TEXT)
['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '12', '', '', '', '', '1961', '', '', '', '', '6', '', '07', '', '', '', '', '']


Examples
--------
* ``[0-9]{2}`` - exactly two digits from `0` to `9`
* ``\d{2}`` - exactly two digits from `0` to `9`
* ``[A-Z]{2,10}`` - two to ten uppercase letters from `A` to `Z`
* ``[A-Z]{2-10}-[0-9]{,5}`` - two to ten uppercase letters from `A` to `Z` followed by dash (`-`) and at least five numbers
* ``[a-z]+`` - at least one lowercase letter from `a` to `z`, but try to fit the longest match
* ``\d+`` - number
* ``\d+\.\d+`` - float


Use Case - 0x01
---------------
* Float

>>> import re
>>>
>>>
>>> TEXT = 'Pi number is 3.1415...'
>>>
>>> pi = re.findall('\d+\.\d+', TEXT)
>>> pi
['3.1415']


Use Case - 0x02
---------------
* Time

>>> import re
>>>
>>>
>>> TEXT = 'Yuri Gagarin launched to space on Apr 12th, 1961 at 6:07 am.'
>>>
>>> re.findall('\d\d:\d\d', TEXT)
[]
>>>
>>> re.findall('\d\d?:\d\d', TEXT)
['6:07']


Use Case - 0x03
---------------
* Date

>>> import re
>>> from datetime import datetime
>>>
>>>
>>> TEXT = 'Yuri Gagarin launched to space on Apr 12th, 1961 at 6:07 am.'
>>>
>>>
>>> result = re.findall('[A-Z][a-z]{2} \d{2}th, \d{4}', TEXT)
>>> result
['Apr 12th, 1961']
>>> datetime.strptime(result[0], '%b %dth, %Y').date()
datetime.date(1961, 4, 12)


Use Case - 0x04
---------------
>>> import re
>>>
>>>
>>> line = 'value=123'
>>>
>>> re.findall(r'(\w+)\s?=\s?(\d+)', line)
[('value', '123')]

>>> import re
>>>
>>>
>>> line = 'value = 123'
>>>
>>> re.findall(r'(\w+)\s?=\s?(\d+)', line)
[('value', '123')]


Use Case - 0x05
---------------
>>> import re
>>> HTML = '<h1>Header 1</h1><p>Paragraph 1</p><p>Paragraph 2</p>'
>>>
>>>
>>> re.findall('<p>.*</p>', HTML)
['<p>Paragraph 1</p><p>Paragraph 2</p>']
>>>
>>> re.findall('<p>.*?</p>', HTML)
['<p>Paragraph 1</p>', '<p>Paragraph 2</p>']


Use Case - 0x06
---------------
>>> import re
>>> HTML = '<h1>Header 1</h1><p>Paragraph 1</p><p>Paragraph 2</p>'
>>>
>>>
>>> re.findall('<p>', HTML)
['<p>', '<p>']
>>>
>>> re.findall('</p>', HTML)
['</p>', '</p>']
>>>
>>> re.findall('</?p>', HTML)
['<p>', '</p>', '<p>', '</p>']


Use Case - 0x07
---------------
>>> import re
>>> HTML = '<h1>Header 1</h1><p>Paragraph 1</p><p>Paragraph 2</p>'
>>>
>>>
>>> re.findall('<.+>', HTML)
['<h1>Header 1</h1><p>Paragraph 1</p><p>Paragraph 2</p>']
>>>
>>> re.findall('<.+?>', HTML)
['<h1>', '</h1>', '<p>', '</p>', '<p>', '</p>']
>>>
>>> re.findall('</?.+?>', HTML)
['<h1>', '</h1>', '<p>', '</p>', '<p>', '</p>']
>>>
>>> re.findall('</?(.+?)>', HTML)
['h1', 'h1', 'p', 'p', 'p', 'p']
>>>
>>> tags = re.findall('</?(.+?)>', HTML)
>>> sorted(set(tags))
['h1', 'p']


Use Case - 0x08
---------------
>>> import re
>>> HTML = '<h1>Header 1</h1><p>Paragraph 1</p><p>Paragraph 2</p>'
>>>
>>>
>>> re.findall('</?.*>', HTML)
['<h1>Header 1</h1><p>Paragraph 1</p><p>Paragraph 2</p>']
>>>
>>> re.findall('</?.*?>', HTML)
['<h1>', '</h1>', '<p>', '</p>', '<p>', '</p>']
