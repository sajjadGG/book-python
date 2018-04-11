import datetime

DATA = {
    "datetime": datetime.datetime(1961, 4, 12, 2, 7, 0, 123456),
    "astronaut": {
        "date": datetime.date(1923, 11, 18),
        "person": "jose.jimenez@nasa.gov"
    },
    "flight": [
        {"datetime": datetime.datetime(1961, 5, 5, 14, 34, 13), "action": "launch"},
        {"datetime": datetime.datetime(1961, 5, 5, 14, 49, 35), "action": "landing"}
    ]
}