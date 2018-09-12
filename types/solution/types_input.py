name = input('Type your name: ')

text = f"""'''My name... "{name}".\n\tI\'m an \"""astronaut!\"""'''"""

output = text.replace(' ', '_').replace('\t', '_')

print(output)
# '''My_name_"José_Jiménez".
# _I'm_an_"""astronaut!"""'''
