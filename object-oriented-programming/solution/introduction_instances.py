class Contact:
    def __init__(self, first_name, last_name, date_of_birth):
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.date_of_birth: str = date_of_birth


class Address:
    def __init__(self, center, city, state):
        self.center: str = center
        self.city: str = city
        self.state: str = state


Contact('Jan', 'Twardowski', '1961-04-12')
Contact('Mark', 'Watney', '1969-07-21')
Address('Kennedy Space Center', 'Merritt Island', 'Florida')
Address('Johnson Space Center', 'Houston', 'Texas')
Address('Jet Propulsion Laboratory', 'Pasadena', 'Texas')
