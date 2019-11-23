expected = 'Jana Twardowskiego III'
text = 'UL. jana \tTWArdoWskIEGO 3'

text = text.title()
text = text.replace('\t', '')
text = text.replace('3', 'III')
text = text.replace('Ul.', '')
text = text.strip()

print(f'{text == expected}\t"{text}"')
