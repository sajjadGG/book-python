import re

re.split(r'\sAND\s', 'Baked Beans And Spam', flags=re.IGNORECASE)
# ['Baked Beans', 'Spam']
