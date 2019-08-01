DATA = {'username': 'Иван Иванович', 'agency': 'Roscosmos'}


def asd(x):
    return x.replace('Иван', 'Ivan')


out = {
    value: asd(value)
    for key, value in DATA.items()
    if key == 'username'
}
# {'Иван Иванович': 'Ivan Ivanоvic'}


out = ['CCCP' if k == 'Roscosmos' else 'USA' for k,v in DATA.items() if k == 'agency']
print(out)
# ['USA']

