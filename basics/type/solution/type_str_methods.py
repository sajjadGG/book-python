expected = 'Jana Twardowskiego III'
text = 'UL. jana \tTWArdoWskIEGO 3'

# Convert to common format
text = text.upper()

# Remove unwanted whitespaces
text = text.replace('\t', '')

# Remove unwanted special characters
text = text.replace('.', '')

# Remove unwanted text
text = text.replace('UL', '')
text = text.replace('3', 'III')

# Formatting
text = text.title()
text = text.replace('Iii', 'III')
text = text.strip()

print('Matched:', text == expected)
# Matched: True

print(text)
# Jana Twardowskiego III
