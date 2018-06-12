*********************************************
CI/CD - Continuous Integration and Deployment
*********************************************

Bitbucket Pipelines
===================
.. code-block:: yaml

    image: python:3.6.5

    clone:
      depth: full

    pipelines:
      default:
        - parallel:
          - step:
              name: "Type Checking"
              caches:
                - pip
              script:
                - pip install mypy
                - python -m mypy --ignore-missing-imports bin
                - python -m mypy --ignore-missing-imports client
                # - python -m mypy --ignore-missing-imports habitat
          - step:
              name: "PEP-8 compliance"
              caches:
                - pip
              script:
                - pip install pycodestyle
                - python -m pycodestyle bin
                - python -m pycodestyle client --ignore=E402
                - python -m pycodestyle habitat
          - step:
              name: "Tests"
              caches:
                - pip
              script:
                - pip install -r requirements.txt
                - pip freeze
                - python manage.py check
                - python manage.py test habitat.tests --verbosity=2
          - step:
             name: "Static Code Analysis"
             image: java:8
             script:
                - curl --insecure -OL https://sonarsource.bintray.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-3.2.0.1227.zip
                - unzip sonar-scanner-cli-*.zip
                - ./sonar-scanner-*/bin/sonar-scanner

        - step:
            name: "Deployment"
            deployment: production
            trigger: automatic
            script:
              - git push --force https://heroku:$HEROKU_API_KEY@git.heroku.com/$HEROKU_APP_NAME.git HEAD

Travis
======
.. code-block:: yaml

    dist: trusty
    sudo: required
    language: python
    python:
      - 3.6.5

    addons:
      sonarcloud:
        organization: "astromatt"

    jdk:
      - oraclejdk8

    cache:
      directories:
        - '$HOME/.sonar/cache'

    install:
      - python -m pip install -r requirements.txt

    script:
      - python -m mypy bin
      - python -m mypy client
      - python -m mypy habitat
      - python -m pycodestyle bin
      - python -m pycodestyle client --ignore=E402
      - python -m pycodestyle habitat
      - python manage.py check
      - python manage.py test habitat.tests --verbosity=2

    after_success:
      - sonar-scanner --debug