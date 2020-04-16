Contribution Guide
==================

Walter's code is currently hosted `on GitHub at excitedleigh/walter <https://github.com/excitedleigh/walter>`_.

Setting Up
----------

.. TODO::

    Update this for the changes to Poetry et al

- To install Walter for development, run ``pip install -e .[dev,docs]``.
- Tests are written using pytest; just run the command ``pytest`` to run them.
- Documentation is built with Sphinx. You can just run ``cd docs; make html`` and browse the generated HTML files, but if you install `devd <https://github.com/cortesi/devd>`_ and `modd <https://github.com/cortesi/modd>`_, then run the command ``modd``, you'll get a nice live-reloading view served on localhost port 8000 (or run e.g. ``env PORT=1337 modd`` to serve on a different port).
