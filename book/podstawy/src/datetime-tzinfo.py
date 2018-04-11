import datetime

# timezone naive - nieświadome
datetime.datetime.now()
datetime.datetime(1957, 10, 4, 19, 28, 34)


# timezone aware - świadome
datetime.datetime.now().replace(tzinfo=datetime.timezone.utc)
datetime.datetime(1957, 10, 4, 19, 28, 34).replace(tzinfo=datetime.timezone.utc)