from datetime import date, datetime
from random import randint

YEAR = 365.2524


class Client:
    def __init__(self, first_name, last_name, date_of_birth=None, is_married=None, is_working=None, has_kids=None, accounts=()):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.is_married = is_married
        self.is_working = is_working
        self.has_kids = has_kids
        self.accounts = list(accounts)

    def age(self):
        age = (datetime.now().date() - self.date_of_birth)
        return round(age.days / YEAR)

    def calculate_scoring(self):
        score = 0

        if self.is_married:
            score += 10
        if self.is_working:
            score += 200
        if self.has_kids:
            score -= 50

        score += self.age() * 10
        score += len(self.accounts) * 20
        score += sum(x.saldo for x in self.accounts)

        return score


class Account:
    TYP = None

    def __init__(self, balance=0.0, currency='PLN'):
        self.balance = balance
        self.currency = currency
        self.number = randint(0, 1e24)
        self.interest_rate = None


class CorporateAccount(Account):
    TYP = 'Corporate'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.interest_rate = 1.0


class CurrencyAccount(Account):
    TYP = 'Currency'

    def __init__(self, currency, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.interest_rate = 1.19


class SavingsAccount(Account):
    TYP = 'Savings'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.interest_rate = 0.0


twardowski = Client(
    first_name='Jan',
    last_name='Twardowski',
    date_of_birth=date(1970, 1, 1),
    has_kids=True,
    is_working=True,
    is_married=True,
    accounts=[
        SavingsAccount(),
        SavingsAccount(),
        CurrencyAccount('EUR'),
    ]
)

if __name__ == '__main__':
    twardowski.calculate_scoring()
