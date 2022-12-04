Modules pyproject.toml
======================
* https://packaging.python.org/en/latest/tutorials/packaging-projects/
* https://peps.python.org/pep-0517/
* https://peps.python.org/pep-0518/
* https://peps.python.org/pep-0621/
* https://peps.python.org/pep-0660/

Modern Python packages can contain a pyproject.toml file, first introduced
in PEP 518 and later expanded in PEP 517, PEP 621 and PEP 660. This file
contains build system requirements and information, which are used by pip
to build the package. [#pyproject]_

.. code-block:: toml

    [project]
    name = "szkolenia-lotnicze"
    version = "0.1.1"
    requires-python = ">=3.11"
    license.file = "LICENSE"  # https://peps.python.org/pep-0639/#add-license-files-key
    authors = [{name = "Mark Watney", email = "mwatney@nasa.gov"}]
    urls.homepage = "https://github.com/AstroMatt/szkolenia-lotnicze"
    urls.repository = "https://github.com/AstroMatt/szkolenia-lotnicze.git"
    urls.documentation = "https://github.com/AstroMatt/szkolenia-lotnicze"
    urls.bugtracker = "https://github.com/AstroMatt/szkolenia-lotnicze/issues"
    dynamic = ["readme"]
    keywords = [
        "ares",
        "mars",
        "nasa",
        "human-spaceflight"]
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 4.1",
        "Intended Audience :: Other Audience",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Natural Language :: English",
        "Natural Language :: Polish",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application"]

    # https://peps.python.org/pep-0440/#version-specifiers
    dependencies = [
        "django == 4.1.*",
        "django-ninja == 0.19.*"]
    optional-dependencies.test = [
        "mypy",
        "pylint",
        "coverage"]


    ## Console scripts
    # Builder will install a shell script named `myapp-cli` in venv's
    # bin directory: `.venv-py311/bin/myapp-cli`

    [project.scripts]
    myapp-cli = "myapp:cli"

    [project.gui-scripts]
    myapp-gui = "myapp:gui"

    [project.entry-points."myapp.run"]
    run = "myapp:run"


    ## Build System

    # [build-system]
    # requires = ["flit"]
    # build-backend = "flit.buildapi"

    [build-system]
    requires = ['setuptools >= 65.6']
    build-backend = 'setuptools.build_meta'

    [tool.setuptools.packages.find]
    where = ["."]
    exclude = ["aviation.*.tests*"]

    [tool.setuptools.dynamic]
    readme.file = "README.rst"
    # version.attr = "aviation.__version__"  ## if 'version' in dynamic


    ## External Tools Configuration

    # https://ichard26-testblackdocs.readthedocs.io/en/refactor_docs/pyproject_toml.html
    [tool.black]
    line-length = 79
    target_version = ["py311"]
    include = '\.pyi?$'
    exclude = '''(
          \.git
        | \.mypy_cache
        | \.venv
        | build
        | dist
    )'''

    # https://mypy.readthedocs.io/en/stable/config_file.html
    # https://mypy.readthedocs.io/en/stable/config_file.html#using-a-pyproject-toml-file
    [tool.mypy]
    python_version = "3.11"
    files = ["src"]
    modules = ["aviation"]
    exclude = [
        '*.egg-info',
        ".git",
        ".mypy_cache",
        "build",
        "dist"]
    warn_return_any = true
    warn_unused_configs = true
    # namespace_packages = false
    # explicit_package_bases = false
    # ignore_missing_imports = false
    # follow_imports = "normal"
    # follow_imports_for_stubs = false
    # no_site_packages = false
    # no_silence_site_packages = false
    # # Platform configuration
    # platform = "linux-64"
    # # Disallow dynamic typing
    # disallow_any_unimported = false # TODO
    # disallow_any_expr = false # TODO
    # disallow_any_decorated = false # TODO
    # disallow_any_explicit = false # TODO
    # disallow_any_generics = true
    # disallow_subclassing_any = true
    # # Untyped definitions and calls
    # disallow_untyped_calls = true
    # disallow_untyped_defs = true
    # disallow_incomplete_defs = true
    # check_untyped_defs = true
    # disallow_untyped_decorators = true
    # # None and Optional handling
    # no_implicit_optional = true
    # strict_optional = true
    # # Configuring warnings
    # warn_redundant_casts = true
    # warn_unused_ignores = true
    # warn_no_return = true
    # warn_return_any = true
    # warn_unreachable = false # GH#27396
    # # Suppressing errors
    # show_none_errors = true
    # ignore_errors = false
    # enable_error_code = "ignore-without-code"
    # # Miscellaneous strictness flags
    # allow_untyped_globals = false
    # allow_redefinition = false
    # local_partial_types = false
    # implicit_reexport = true
    # strict_equality = true
    # # Configuring error messages
    # show_error_context = false
    # show_column_numbers = false
    # show_error_codes = true


    [tool.isort]
    line_length = 79
    src_paths = ["requests", "test"]
    combine_as_imports = true
    skip_gitignore = true
    honor_noqa = true
    atomic = true
    profile = "black"
    skip_glob = ["tests/*"]
    known_first_party = ["black", "blackd"]


    # https://github.com/pytest-dev/pytest/blob/main/pyproject.toml
    [tool.pytest.ini_options]
    testpaths = ["tests"]
    addopts = "--strict-config --strict-markers --doctest-modules"
    doctest_optionflags = "NORMALIZE_WHITESPACE ELLIPSIS"
    python_files = ["test_*.py", "*_test.py", "test/*.py", "tests/*.py"]


    # pylint --generate-toml-config >> pyproject.toml
    [tool.pylint]
    max-line-length = 79
    ignore = [".git"]
    good-names = ["i", "j", "k", "x", "Run", "_"]
    design.max-args = 5                     # Maximum number of arguments for function / method.
    design.max-attributes = 7               # Maximum number of attributes for a class (see R0902).
    design.max-bool-expr = 5                # Maximum number of boolean expressions in an if statement (see R0916).
    design.max-branches = 12                # Maximum number of branch for function / method body.
    design.max-locals = 15                  # Maximum number of locals for function / method body.
    design.max-parents = 7                  # Maximum number of parents for a class (see R0901).
    design.max-public-methods = 20          # Maximum number of public methods for a class (see R0904).
    design.max-returns = 6                  # Maximum number of return / yield for function / method body.
    design.max-statements = 50              # Maximum number of statements in function / method body.
    design.min-public-methods = 2           # Minimum number of public methods for a class (see R0903).
    format.ignore-long-lines = "^(\\s*(# )?<?https?://\\S+>?$|.*models.))"  # Regexp for a line that is allowed to be longer than the limit.
    format.max-line-length = 79             # Maximum number of characters on a single line.
    format.max-module-lines = 1000          # Maximum number of lines in a module.
    logging.logging-format-style = "new"    # The type of string formatting that logging methods do. `old` means using % formatting, `new` is for `{}` formatting.
    logging.logging-modules = ["logging"]   # Logging modules to check that the string format arguments are in logging function parameter format.
    refactoring.max-nested-blocks = 5       # Maximum number of nested blocks for function / method body
    reports.output-format = "parseable"     # Set the output format. Available formats are text, parseable, colorized, json, and msvs (visual studio)
    reports.reports = true                  # Tells whether to display a full report or only the messages.
    reports.score = true                    # Activate the evaluation score.
    similarities.min-similarity-lines = 4   # Minimum lines number of a similarity.
    disable = [
        "missing-module-docstring",         # "C0114"
        "missing-class-docstring",          # "C0115"
        "missing-function-docstring",       # "C0116"
        "too-few-public-methods",           # "R0903"
        "too-many-arguments",               # "R0913"
    ]

Verify ``pip install .``


References
----------
.. [#pyproject] Pip developers. "pyproject.toml". Year: 2022. Retrieved: 2022-12-01. URL: https://pip.pypa.io/en/stable/reference/build-system/pyproject-toml/
