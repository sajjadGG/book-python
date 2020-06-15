def clean(text: str) -> str:
    """
    >>> DATA = [
    ...     'ul.Mieszka II',
    ...     'UL. Zygmunta III WaZY',
    ...     '  bolesława chrobrego ',
    ...     'ul Jana III SobIESkiego',
    ...     '\tul. Jana trzeciego Sobieskiego',
    ...     'ulicaJana III Sobieskiego',
    ...     'UL. JA    NA 3 SOBIES  KIEGO',
    ...     'ULICA JANA III SOBIESKIEGO  ',
    ...     'ULICA. JANA III SOBIeskieGO',
    ...     ' Jana 3 Sobieskiego  ',
    ...     'Jana III Sobi  eskiego ',
    ... ]
    >>> for address in DATA:
    ...     clean(address)
    'Mieszka II'
    'Zygmunta III Wazy'
    'Bolesława Chrobrego'
    'Jana III Sobieskiego'
    'Jana III Sobieskiego'
    'Jana III Sobieskiego'
    'Jana III Sobieskiego'
    'Jana III Sobieskiego'
    'Jana III Sobieskiego'
    'Jana III Sobieskiego'
    'Jana III Sobieskiego'
    """

    # Convert to common format
    text = text.upper()

    # Remove unwanted whitespaces
    text = text.replace('\n', '')
    text = text.replace('\t', '')
    text = text.replace('     ', '')
    text = text.replace('    ', '')
    text = text.replace('   ', '')
    text = text.replace('  ', '')

    # Remove unwanted special characters
    text = text.replace('.', '')
    text = text.replace(',', '')
    text = text.replace('-', '')
    text = text.replace('|', '')

    # Remove unwanted text
    text = text.replace('ULICA', '')
    text = text.replace('UL', '')
    text = text.replace('TRZECIEGO', 'III')
    text = text.replace('3', 'III')

    # Formatting
    text = text.title()
    text = text.replace('Iii', 'III')
    text = text.replace('Ii', 'II')

    # Return
    return text.strip()
