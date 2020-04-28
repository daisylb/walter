Contribution guide
==================

Walter's code is currently hosted `on GitHub at excitedleigh/walter <https://github.com/excitedleigh/walter>`_.

Setting Up
----------

- First, `install Poetry <https://python-poetry.org/docs/#installation>`_. Then, run ``poetry install``.
- Tests are written using pytest; run ``poetry run pytest`` to run them.

    - To run tests on all of the Python versions Walter supports, run ``poetry run nox``. Note that you'll need to have all of the versions in question installed and available for Nox to find.

- Documentation is built with Sphinx. You can just run ``cd docs; poetry run make html`` and browse the generated HTML files, but if you install `devd <https://github.com/cortesi/devd>`_ and `modd <https://github.com/cortesi/modd>`_, then run the command ``modd``, you'll get a nice live-reloading view served on localhost port 8000 (or run e.g. ``env PORT=1337 modd`` to serve on a different port).