from datetime import datetime, timezone
from pprint import pprint


# https://history.nasa.gov/SP-4029/Apollo_11i_Timeline.htm
INPUT = """
1969-07-14, 21:00:00, UTC, INFO, Terminal countdown started
1969-07-16, 13:31:53, UTC, WARNING, S-IC engine ignition (#5)
1969-07-16, 13:33:23, UTC, DEBUG, Maximum dynamic pressure (735.17 lb/ft^2)
1969-07-16, 13:34:44, UTC, WARNING, S-II ignition
1969-07-16, 13:35:17, UTC, DEBUG, Launch escape tower jettisoned
1969-07-16, 13:39:40, UTC, DEBUG, S-II center engine cutoff
1969-07-16, 16:22:13, UTC, INFO, Translunar injection
1969-07-16, 16:56:03, UTC, INFO, CSM docked with LM/S-IVB
1969-07-16, 17:21:50, UTC, INFO, Lunar orbit insertion ignition
1969-07-16, 21:43:36, UTC, INFO, Lunar orbit circularization ignition
1969-07-20, 17:44:00, UTC, INFO, CSM/LM undocked
1969-07-20, 20:05:05, UTC, WARNING, LM powered descent engine ignition
1969-07-20, 20:10:22, UTC, ERROR, LM 1202 alarm
1969-07-20, 20:14:18, UTC, ERROR, LM 1201 alarm
1969-07-20, 20:17:39, UTC, WARNING, LM lunar landing
1969-07-21, 02:39:33, UTC, DEBUG, EVA started (hatch open)
1969-07-21, 02:56:15, UTC, WARNING, 1st step taken lunar surface (CDR)
1969-07-21, 02:56:15, UTC, WARNING, That's one small step for [a] man... one giant leap for mankind
1969-07-21, 03:05:58, UTC, DEBUG, Contingency sample collection started (CDR)
1969-07-21, 03:15:16, UTC, INFO, LMP on lunar surface
1969-07-21, 05:11:13, UTC, DEBUG, EVA ended (hatch closed)
1969-07-21, 17:54:00, UTC, WARNING, LM lunar liftoff ignition (LM APS)
1969-07-21, 21:35:00, UTC, INFO, CSM/LM docked
1969-07-22, 04:55:42, UTC, WARNING, Transearth injection ignition (SPS)
1969-07-24, 16:21:12, UTC, INFO, CM/SM separation
1969-07-24, 16:35:05, UTC, WARNING, Entry
1969-07-24, 16:50:35, UTC, WARNING, Splashdown (went to apex-down)
1969-07-24, 17:29, UTC, INFO, Crew egress
"""

OUTPUT = []


for line in INPUT.splitlines():
    if not line:
        continue

    date, time, timezone, level, message = line.split(', ', maxsplit=4)
    date = datetime.strptime(date, '%Y-%m-%d')

    try:
        time = datetime.strptime(time, '%H:%M:%S').time()
    except ValueError:
        time = datetime.strptime(time, '%H:%M').time()

    OUTPUT.append({
        'date': datetime.combine(date, time),
        'timezone': timezone,
        'level': level,
        'message': message,
    })

pprint(OUTPUT)
