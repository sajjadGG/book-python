def clean(text: str) -> str:
    """
    >>> clean('  bolesława chrobrego ')
    'Bolesława Chrobrego'

    >>> clean('ul Jana III SobIESkiego')
    'Jana III Sobieskiego'

    >>> clean('\tul. Jana trzeciego Sobieskiego')
    'Jana III Sobieskiego'

    >>> clean('ulicaJana III Sobieskiego')
    'Jana III Sobieskiego'

    >>> clean('UL. JA\tNA 3 SOBIES  KIEGO')
    'Jana III Sobieskiego'

    >>> clean('UL. Zygmunta III WaZY')
    'Zygmunta III Wazy'

    >>> clean('ULICA JANA III SOBIESKIEGO  ')
    'Jana III Sobieskiego'

    >>> clean('ULICA. JANA III SOBIeskieGO')
    'Jana III Sobieskiego'

    >>> clean(' Jana 3 Sobieskiego  ')
    'Jana III Sobieskiego'

    >>> clean(' Jana 3ego Sobieskiego  ')
    'Jana III Sobieskiego'

    >>> clean('Jana III Sobi\teskiego ')
    'Jana III Sobieskiego'

    >>> clean('ul.Mieszka II')
    'Mieszka II'
    """

    # Common format
    text = text.upper()

    # Remove unwanted parts
    text = text.replace('ULICA', '')
    text = text.replace('UL', '')
    text = text.replace('TRZECIEGO', 'III')
    text = text.replace('3EGO', 'III')
    text = text.replace('3', 'III')
    text = text.replace('.', '')

    # Clean whitespaces
    text = text.replace('\n', '')
    text = text.replace('\t', '')
    text = text.replace('    ', '')
    text = text.replace('   ', '')
    text = text.replace('  ', '')
    text = text.strip()

    # Formatting
    text = text.title()
    text = text.replace('Iii', 'III')
    text = text.replace('Ii', 'II')

    # Return
    return text
