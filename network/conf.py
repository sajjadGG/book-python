import sys; sys.path.append('..')
from conf import *

project = 'Python: Network'
author = 'Matt Harasymczuk'
email = 'matt@astrotech.io'

todo_emit_warnings = True
todo_include_todos = True

html_favicon = '../_static/favicon.png'
html_static_path = ['../_static']
html_context = {
    'css_files': ['_static/dark.css', '_static/print.css'],
    'script_files': ['_static/jquery.min.js', '_static/onload.js']}
