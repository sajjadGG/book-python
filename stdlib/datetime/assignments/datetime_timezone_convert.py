"""
* Assignment: Datetime Timezone Convert
* Complexity: easy
* Lines of code: 5 lines
* Time: 13 min

English:
    1. Use data from "Given" section (see below)
    2. Create `timezone` object of:
        a. UTC
        b. London, United Kingdom
        c. Moscow, Russian Federation
        d. Warsaw, Poland
        e. Tokyo, Japan
        f. Sydney, Australia
        g. Auckland, New Zealand
        h. New York, USA
    3. Use `List of tz database time zones` [1]

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Stwórz obiekt `timezone` z:
        a. UCT
        b. London, Wielka Brytania
        c. Moscow, Rosja
        d. Warsaw, Polska
        e. Tokyo, Japan
        f. Sydney, Australia
        g. Auckland, Nowa Zelandia
        h. New York, USA
    3. Użyj `List of tz database time zones` [1]

References:
    [1] Wikipedia. List of tz database time zones.
        URL: https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
        Accessed Date: 2021-03-24
    [2] IANA. Time Zone Database.
        URL: https://data.iana.org/time-zones/releases/
        Accessed Date: 2021-03-24

Extra Task:
    1. Cape Canaveral, FL, USA
    2. Houston, TX, USA
    3. Bajkonur Cosmodrome, Kazachstan
    5. North Pole
    6. South Pole


Tests:
    >>> utc
    <UTC>
    >>> london
    <DstTzInfo 'Europe/London' LMT-1 day, 23:59:00 STD>
    >>> moscow
    <DstTzInfo 'Europe/Moscow' LMT+2:30:00 STD>
    >>> warsaw
    <DstTzInfo 'Europe/Warsaw' LMT+1:24:00 STD>
    >>> tokyo
    <DstTzInfo 'Asia/Tokyo' LMT+9:19:00 STD>
    >>> sydney
    <DstTzInfo 'Australia/Sydney' LMT+10:05:00 STD>
    >>> auckland
    <DstTzInfo 'Pacific/Auckland' LMT+11:39:00 STD>
    >>> new_york
    <DstTzInfo 'America/New_York' LMT-1 day, 19:04:00 STD>
    >>> cape_canaveral
    <DstTzInfo 'America/New_York' LMT-1 day, 19:04:00 STD>
    >>> houston
    <DstTzInfo 'America/Chicago' LMT-1 day, 18:09:00 STD>
    >>> bajkonur
    <DstTzInfo 'Asia/Almaty' LMT+5:08:00 STD>
    >>> north_pole
    <DstTzInfo 'Arctic/Longyearbyen' LMT+0:43:00 STD>
    >>> south_pole
    <DstTzInfo 'Europe/Warsaw' LMT+1:24:00 STD>
"""


# Given
from pytz import timezone


utc: timezone = ...  # timezone in UTC
london: timezone = ...  # timezone in London, United Kingdom
moscow: timezone = ...  # timezone in Moscow, Russian Federation
warsaw: timezone = ...  # timezone in Warsaw, Poland
tokyo: timezone = ...  # timezone in Tokyo, Japan
sydney: timezone = ...  # timezone in Sydney, Australia
auckland: timezone = ...  # timezone in Auckland, New Zealand
new_york: timezone = ...  # timezone in New York, USA

cape_canaveral: timezone = ...  # timezone in Cape Canaveral, FL, USA
houston: timezone = ...  # timezone in Houston, TX, USA
bajkonur: timezone = ...  # timezone in Bajkonur Cosmodrome, Kazachstan
north_pole: timezone = ...  # timezone in North Pole
south_pole: timezone = ...  # timezone in South Pole


# Solution
utc = timezone('UTC')
london = timezone('Europe/London')
moscow = timezone('Europe/Moscow')
warsaw = timezone('Europe/Warsaw')
tokyo = timezone('Asia/Tokyo')
sydney = timezone('Australia/Sydney')
auckland = timezone('Pacific/Auckland')
new_york = timezone('America/New_York')

cape_canaveral = timezone('America/New_York')
houston = timezone('America/Chicago')
bajkonur = timezone('Asia/Almaty')
north_pole = timezone('Arctic/Longyearbyen')
south_pole = timezone('Europe/Warsaw')

