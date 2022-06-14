Wheel
=====
* https://github.com/pypa/cibuildwheel


CI/CD
-----
* ``.github/workflows/wheels.yml``
* Source https://github.com/pypa/cibuildwheel

.. code-block:: yaml

    name: Build

    on: [push, pull_request]

    jobs:
      build_wheels:
        name: Build wheels on ${{ matrix.os }}
        runs-on: ${{ matrix.os }}
        strategy:
          matrix:
            os: [ubuntu-20.04, windows-2019, macOS-10.15]

        steps:
          - uses: actions/checkout@v2

          # Used to host cibuildwheel
          - uses: actions/setup-python@v2

          - name: Install cibuildwheel
            run: python -m pip install cibuildwheel==2.6.1

          - name: Build wheels
            run: python -m cibuildwheel --output-dir wheelhouse
            # to supply options, put them in 'env', like:
            # env:
            #   CIBW_SOME_OPTION: value

          - uses: actions/upload-artifact@v2
            with:
              path: ./wheelhouse/*.whl

Config
------
* ``pyproject.toml``
* Source: https://github.com/numpy/numpy/blob/main/pyproject.toml

.. code-block:: toml

    [tool.cibuildwheel]
    skip = "cp36-* cp37-* pp37-* *-manylinux_i686 *_ppc64le *_s390x *-musllinux*"
    build-verbosity = "3"
    before-build = "bash {project}/tools/wheels/cibw_before_build.sh {project}"
    before-test = "pip install -r {project}/test_requirements.txt"
    test-command = "bash {project}/tools/wheels/cibw_test_command.sh {project}"

    [tool.cibuildwheel.linux]
    manylinux-x86_64-image = "manylinux2014"
    manylinux-aarch64-image = "manylinux2014"
    environment = { CFLAGS="-std=c99 -fno-strict-aliasing", LDFLAGS="-Wl,--strip-debug", OPENBLAS64_="/usr/local", NPY_USE_BLAS_ILP64="1", RUNNER_OS="Linux" }

    [tool.cibuildwheel.macos]
    # For universal2 wheels, we will need to fuse them manually
    # instead of going through cibuildwheel
    # This is because cibuildwheel tries to make a fat wheel
    # https://github.com/multi-build/multibuild/blame/devel/README.rst#L541-L565
    # for more info
    archs = "x86_64 arm64"
    test-skip = "*_arm64 *_universal2:arm64"
    # MACOS linker doesn't support stripping symbols
    environment = { CFLAGS="-std=c99 -fno-strict-aliasing", OPENBLAS64_="/usr/local", NPY_USE_BLAS_ILP64="1", CC="clang", CXX = "clang++" }

    [tool.cibuildwheel.windows]
    environment = { OPENBLAS64_="openblas", OPENBLAS="", NPY_USE_BLAS_ILP64="1", CFLAGS="", LDFLAGS="" }

    [[tool.cibuildwheel.overrides]]
    select = "*-win32"
    environment = { OPENBLAS64_="", OPENBLAS="openblas", NPY_USE_BLAS_ILP64="0", CFLAGS="-m32", LDFLAGS="-m32" }
