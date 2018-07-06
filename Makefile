book:
    @rm -fr .build && sphinx-build -j4 -b html . .build/

help:
    @sphinx-build -M help help help

clean:
    -rm -fr .build/
