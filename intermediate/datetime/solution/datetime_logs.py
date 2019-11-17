from datetime import datetime, timezone
from pprint import pprint


# https://history.nasa.gov/SP-4029/Apollo_11i_Timeline.htm
INPUT = """
1969-07-14T21:00:00 [INFO] Terminal countdown started
1969-07-16T13:31:53 [WARNING] S-IC engine ignition (#5)
1969-07-16T13:33:23 [DEBUG] Maximum dynamic pressure (735.17 lb/ft^2)
1969-07-16T13:34:44 [WARNING] S-II ignition
1969-07-16T13:35:17 [DEBUG] Launch escape tower jettisoned
1969-07-16T13:39:40 [DEBUG] S-II center engine cutoff
1969-07-16T16:22:13 [INFO] Translunar injection
1969-07-16T16:56:03 [INFO] CSM docked with LM/S-IVB
1969-07-16T17:21:50 [INFO] Lunar orbit insertion ignition
1969-07-16T21:43:36 [INFO] Lunar orbit circularization ignition
1969-07-20T17:44:00 [INFO] CSM/LM undocked
1969-07-20T20:05:05 [WARNING] LM powered descent engine ignition
1969-07-20T20:10:22 [ERROR] LM 1202 alarm
1969-07-20T20:14:18 [ERROR] LM 1201 alarm
1969-07-20T20:17:39 [WARNING] LM lunar landing
1969-07-21T02:39:33 [DEBUG] EVA started (hatch open)
1969-07-21T02:56:15 [WARNING] 1st step taken lunar surface (CDR) "That’s one small step for a man…one giant leap for mankind"
1969-07-21T03:05:58 [DEBUG] Contingency sample collection started (CDR)
1969-07-21T03:15:16 [INFO] LMP on lunar surface
1969-07-21T05:11:13 [DEBUG] EVA ended (hatch closed)
1969-07-21T17:54:00 [WARNING] LM lunar liftoff ignition (LM APS)
1969-07-21T21:35:00 [INFO] CSM/LM docked
1969-07-22T04:55:42 [WARNING] Transearth injection ignition (SPS)
1969-07-24T16:21:12 [INFO] CM/SM separation
1969-07-24T16:35:05 [WARNING] Entry
1969-07-24T16:50:35 [WARNING] Splashdown (went to apex-down)
1969-07-24T17:29 [INFO] Crew egress
"""

OUTPUT = []


for line in INPUT.splitlines():
    if not line:
        continue

    date, level, message = line.split(maxsplit=2)
    level = level.replace('[', '').replace(']', '')

    try:
        date = datetime.strptime(date, '%Y-%m-%dT%H:%M:%S')
    except ValueError:
        date = datetime.strptime(date, '%Y-%m-%dT%H:%M')

    OUTPUT.append({
        'date': date.replace(tzinfo=timezone.utc),
        'level': level,
        'message': message,
    })

pprint(OUTPUT)
