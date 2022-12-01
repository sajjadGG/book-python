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

    [build-system]
    requires = ["flit"]
    build-backend = "flit.buildapi"

    [project]
    name = "Project Name"
    license = "GPL-2.0-only"
    authors = ["Mark Watney <mwatney@nasa.gov>"]
    maintainers = ["Mark Watney <mwatney@nasa.gov>"]

    dynamic = ["version", "readme", "description-file"]
    version = "1.0.0"
    readme = "README.md"
    description-file = "README.md"
    keywords = ["ares", "mars", "nasa"]

    # Classifiers list:
    # https://pypi.org/classifiers/
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
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
    ]

    # https://peps.python.org/pep-0440/#version-specifiers
    requires-python = ">=3.11"
    dependencies = [
        "django ~= 4.1.3",
        "ninja ~= 0.19.1"
    ]
    [project.optional-dependencies]
    test = [
        "mypy",
        "pylint",
        "coverage",
    ]

    [project.urls]
    homepage = "example.com"
    repository = "https://github.com/myuser/myrepo.git"
    documentation = "https://github.com/myuser/myrepo"
    bugtracker = "https://github.com/myuser/myrepo/issues"

    [project.scripts]
    myapp-cli = "myapp:main_cli"

    [project.gui-scripts]
    myapp-gui = "myapp:main_gui"

    [project.entry-points."myapp.magical"]
    tomatoes = "myapp:main_tomatoes"

    [tool.pylint]
    max-line-length = 88
    disable = [
        "C0114", # (missing-module-docstring)
        "C0115", # (missing-class-docstring)
        "C0116", # (missing-function-docstring)
        "R0903", # (too-few-public-methods)
        "R0913", # (too-many-arguments)
    ]

    [tool.black]
    line-length = 120
    target_version = ['py311']
    include = '\.pyi?$'
    exclude = '''

    (
      /(
          \.eggs         # exclude a few common directories in the
        | \.git          # root of the project
        | \.hg
        | \.mypy_cache
        | \.tox
        | \.venv
        | _build
        | buck-out
        | build
        | dist
      )/
      | foo.py           # also separately exclude a file named foo.py in
                         # the root of the project
    )
    '''

    [tool.mypy]
    # Import discovery
    files = ["src"]
    namespace_packages = false
    explicit_package_bases = false
    ignore_missing_imports = false
    follow_imports = "normal"
    follow_imports_for_stubs = false
    no_site_packages = false
    no_silence_site_packages = false
    # Platform configuration
    python_version = "3.10"
    platform = "linux-64"
    # Disallow dynamic typing
    disallow_any_unimported = false # TODO
    disallow_any_expr = false # TODO
    disallow_any_decorated = false # TODO
    disallow_any_explicit = false # TODO
    disallow_any_generics = true
    disallow_subclassing_any = true
    # Untyped definitions and calls
    disallow_untyped_calls = true
    disallow_untyped_defs = true
    disallow_incomplete_defs = true
    check_untyped_defs = true
    disallow_untyped_decorators = true
    # None and Optional handling
    no_implicit_optional = true
    strict_optional = true
    # Configuring warnings
    warn_redundant_casts = true
    warn_unused_ignores = true
    warn_no_return = true
    warn_return_any = true
    warn_unreachable = false # GH#27396
    # Suppressing errors
    show_none_errors = true
    ignore_errors = false
    enable_error_code = "ignore-without-code"
    # Miscellaneous strictness flags
    allow_untyped_globals = false
    allow_redefinition = false
    local_partial_types = false
    implicit_reexport = true
    strict_equality = true
    # Configuring error messages
    show_error_context = false
    show_column_numbers = false
    show_error_codes = true


References
----------
.. [#pyproject] Pip developers. "pyproject.toml". Year: 2022. Retrieved: 2022-12-01. URL: https://pip.pypa.io/en/stable/reference/build-system/pyproject-toml/
