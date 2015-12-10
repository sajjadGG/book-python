import re


TEKST = """
"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
Section 1.10.32 of "de Finibus Bonorum et Malorum", written by Cicero in 45 BC
"Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?"
"""


SLOWA_ZAWIERAJACE_IS = re.compile(r'[a-zA-Z0-9]*is[a-zA-Z0-9]*')
SLOWA_ZAWIERAJACE_IS.findall(TEKST)



import sys
sys.exit()


SLOWA_ZAWIERAJACE_IS = r'[a-zA-Z0-9]*is[a-zA-Z0-9]*'
wynik = re.findall(SLOWA_ZAWIERAJACE_IS, TEKST)
print(wynik)


import sys
sys.exit()



POPRAWNY_EMAIL = r'(^[a-z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)'


def email_poprawny(email):
    if re.match(POPRAWNY_EMAIL, email):
        print('Poprawny:', email)
        return True
    else:
        print('Niepoprawny:', email)
        return False


email_poprawny('Amatt@astrotech.io')
email_poprawny('matt@astrotech.io')
email_poprawny('+matt@astrotech.io')
email_poprawny('matt+@astrotech.io')
email_poprawny('mattastrotech@.io')
