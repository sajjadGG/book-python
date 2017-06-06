import subprocess
import datetime


def get_version():
    return '#{sha1}, {date:%Y-%m-%d}'.format(
        sha1=subprocess.Popen('git log -1 --format="%h"', stdout=subprocess.PIPE, shell=True).stdout.read().decode().replace('\n', ''),
        date=datetime.date.today(),
    )


extensions = [
    #'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    #'sphinx.ext.githubpages',
    #'sphinx.ext.todo',
    #'sphinx.ext.coverage',
    'sphinx.ext.imgmath',
    #'sphinx.ext.pngmath',
    #'sphinx.ext.viewcode',
]

templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
project = 'Python Workshop'
copyright = '2015-2017, Matt Harasymczuk'
author = 'Matt Harasymczuk'
version = get_version()
release = get_version()
language = 'pl'
exclude_patterns = ['_build', '_themes', 'README.rst']
pygments_style = 'vs'
todo_include_todos = True
today_fmt = '%Y-%m-%d'

html_theme = 'sphinx_rtd_theme'
html_theme_path = ['_themes']
html_static_path = []
html_sidebars = {'sidebar': ['localtoc.html', 'sourcelink.html', 'searchbox.html']}
html_show_sphinx = False
htmlhelp_basename = 'PythonWorkshop'

latex_elements = {}
latex_documents = [
  (master_doc, 'Python-Workshop.tex', 'Python Workshop', 'Matt Harasymczuk', 'manual'),
]

man_pages = [
    (master_doc, 'python-workshop', 'Python Workshop', [author], 1)
]

texinfo_documents = [
  (master_doc, 'Python-Workshop', 'Python Workshop', author, 'Python Workshop', '', 'Miscellaneous'),
]

epub_title = project
epub_author = author
epub_publisher = author
epub_copyright = copyright
epub_exclude_files = ['search.html']
