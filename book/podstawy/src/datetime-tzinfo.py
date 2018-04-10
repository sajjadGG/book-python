import datetime

# timezone naive - nieświadome
datetime.datetime.now()

# timezone aware - świadome
datetime.datetime.now().replace(tzinfo=datetime.timezone.utc)