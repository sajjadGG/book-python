import timeit

setup = """
first_name = 'José'
last_name = 'Jiménez'
"""

test = [
    'name = first_name + " " + last_name',
    'name = f"{first_name} {last_name}"',
    'name = "{0} {1}".format(first_name, last_name)',
    'name = " ".join([first_name, last_name])'
]

for line in test:
    duration = timeit.timeit(stmt=line, setup=setup, number=10000)
    print(f'{duration:.3}\t{line}')

    # 0.0025	name = first_name + " " + last_name
    # 0.00213	name = f"{first_name} {last_name}"
    # 0.00447	name = "{0} {1}".format(first_name, last_name)
    # 0.0028	name = " ".join([first_name, last_name])
