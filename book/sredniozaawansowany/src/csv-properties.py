import csv

FILENAME = r'../contrib/sonar-project.properties'
"""
sonar.host.url=https://sonarcloud.io
sonar.organization=astromatt
sonar.login=...
sonar.language=py
sonar.sourceEncoding=UTF-8
sonar.verbose=true
sonar.projectKey=habitatOS
sonar.projectName=habitatOS
sonar.projectDescription=Operating System for analog extraterrestrial habitats.
sonar.links.homepage=https://bitbucket.org/AstroMatt/habitatOS/
sonar.links.scm=https://bitbucket.org/AstroMatt/habitatOS/
sonar.links.issue=https://bitbucket.org/AstroMatt/habitatOS/issues
sonar.links.ci=https://bitbucket.org/AstroMatt/habitatos/addon/pipelines/home
sonar.projectBaseDir=habitat
sonar.sources=.
sonar.exclusions=**/migrations/**
"""

with open(FILENAME) as file:
    config = csv.DictReader(
        file,
        fieldnames=['property', 'value'],
        delimiter='=',
        lineterminator='\n',
        quoting=csv.QUOTE_NONE)

    for line in config:
        property = line['property']
        value = line['value']
        print(f'{property} -> {value}')
