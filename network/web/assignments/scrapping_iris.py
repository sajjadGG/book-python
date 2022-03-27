"""
>>> result[:5]  # doctest: +NORMALIZE_WHITESPACE
[{'Sepal length': '5.4', 'Sepal width': '3.9', 'Petal length': '1.3', 'Petal width': '0.4', 'Species': 'setosa'},
 {'Sepal length': '5.9', 'Sepal width': '3.0', 'Petal length': '5.1', 'Petal width': '1.8', 'Species': 'virginica'},
 {'Sepal length': '6.0', 'Sepal width': '3.4', 'Petal length': '4.5', 'Petal width': '1.6', 'Species': 'versicolor'},
 {'Sepal length': '7.3', 'Sepal width': '2.9', 'Petal length': '6.3', 'Petal width': '1.8', 'Species': 'virginica'},
 {'Sepal length': '5.6', 'Sepal width': '2.5', 'Petal length': '3.9', 'Petal width': '1.1', 'Species': 'versicolor'}]"""

from bs4 import BeautifulSoup
import requests


URL = 'https://github.com/AstroMatt/book-python/blob/master/_data/csv/iris-dirty.csv'
HEADER = ['Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species']
result = list()


with open('/tmp/iris-dirty.html', mode='w') as file:
    response = requests.get(URL)
    file.write(response.text)

with open('/tmp/iris-dirty.html', mode='r') as file:
    html = BeautifulSoup(file, 'lxml')


table = html.find_all('table')[0]

table_rows = table.find_all('tr')
table_header = table_rows[0]
table_body = table_rows[1:]

species = table_header.text.split()[2:]

for cell in table_body:
    values = cell.text.split()
    values = dict(zip(HEADER, values))
    species_id = int(values['Species'])
    values['Species'] = species[species_id]
    result.append(values)
