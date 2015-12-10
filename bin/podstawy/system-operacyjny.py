import sys
import os
from os.path import join, getsize

# for element in os.scandir('/etc'):
#    print(element.name)


script = os.path.basename(__file__)
PWD = os.path.basename(os.getcwd())

path = os.path.join(PWD, script)

print(path)

print(sys.platform)
