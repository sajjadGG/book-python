from distutils.core import setup, Extension

module = Extension('hello', sources = ['hello-cmodule.c'])


setup(
    name='hello',
    version='1.0',
    description = 'Ehlo World!',
    ext_modules = [module]
)


