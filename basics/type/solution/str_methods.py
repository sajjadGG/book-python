expected = 'Jana Twardowskiego III'
text = 'UL. jana \tTWArdoWskIEGO 3'

text = text.upper()
text = text.replace('UL.', '')
text = text.replace('\t', '')
text = text.replace('3', 'III')
text = text.title()
text = text.replace('Iii', 'III')
text = text.strip()

print('Matched:', text == expected)
# Matched: True

print(text)
# Jana Twardowskiego III
