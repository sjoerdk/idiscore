===========
Development
===========
Some notes

* idiscore is python-only. We recommend pycharm as an editor
* Work via pull requests: clone the idiscore repo, make changes and make a pull request

Code quality
------------
All code must conform to `flake8 <https://pypi.org/project/flake8/>`_. And `black <https://pypi.org/project/black/>`_
Build will fail for non-conformant code.
Either run flake8 and black yourself (in repo root folder, type `flake8 idiscore tests`, and 'black .') or install the pre-commit hooks::

    $ python3 -m pip install pre-commit
    $ python3 -m pre-commit install

This will run black and flake8 automatically before any commit