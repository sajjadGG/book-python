name = input('Type your name: ')
text = f"""'''My name "{name}".\n\tI\'m an \"""astronaut!\"""'''"""
output = text.replace(' ', '_').replace('\t', '_')

print(output)
