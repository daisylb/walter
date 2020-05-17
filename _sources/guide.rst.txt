Guide to using Walter
=====

Projects that use Walter have their configuration defined at the top level of a configuration file. You'll create a Walter :class:`~walter.config.Config` object, then call it to get values out of it.

Using Walter is similar to pulling your configuration out of ``os.environ``, but Walter gives you more options about where your configuration comes from, and more information when your configuration isn't set right.

Setting up your configuration file
-----

To get started, you'll need to create a config object:

.. code-block:: python

    from walter.config import Config

    with Config("Acme Inc.", "My Awesome App") as config:
        ... # all the rest of the code goes in here

There's two things to take note of here:

1. We're passing an author name and a product name into the :class:`~walter.config.Config` object. Walter can load configuration from files on disk, and these two values form part of the paths Walter will look in.
2. All of our configuration goes inside an indented block, surrounded by a context manager. Walter will collect any errors in the values it tries to return, and throw an exception listing all of them when the context manager finishes.

Loading your configuration
-----

From **inside the indented block**, call the ``config`` object.

.. code-block:: python

    with Config("Acme Inc.", "My Awesome App") as config:
        ...
        SECRET_KEY = config('SECRET_KEY')
        ...

You can use the ``cast`` argument to pass a converter function, in cases where you need to parse the string you get back into something different. If the converter function returns an error, it'll be presented to the user in the same manner as missing values.

.. code-block:: python

    import dj_database_url

    with Config("Acme Inc.", "My Awesome App") as config:
        ...
        DEBUG = config('DEBUG', cast=bool)
        DATABASES = {
            'default': config('DATABASE_URL', cast=dj_database_url.parse),
        }
        ...

.. note::

    The ``bool`` built-in is special-cased by Walter; instead of calling it, which will give you ``bool``'s default behaviour of returning ``False`` for an empty string and ``True`` for anything else, Walter does a case-insensitive match on ``t``, ``true``, ``y``, ``yes``, ``f``, ``false``, ``n``, or ``no`` and raises an error if the value doesn't match one of those.

If you want to make a parameter optional, supply the ``default`` argument. (If you supply both ``cast`` and ``default``, the default value is *not* passed to ``cast``.)

.. code-block:: python

    with Config("Acme Inc.", "My Awesome App") as config:
        ...
        SENTRY_DSN = config('SENTRY_DSN', default=None)
        ...

After the indented block, you can then access the variables you created. If they weren't set correctly, Walter will throw an error when the indented block is finished, so that your code using them doesn't run.

.. code-block:: python

    with Config("Acme Inc.", "My Awesome App") as config:
        ...

    database.connect(DATABASES['default'])

Alternatively, you can have your configuration defined in a ``settings.py``, and just import that. (If you're using Walter with Django, for example, your ``settings.py`` can just consist of the Walter indented block and nothing else.)

For more details about config objects, look at the API documentation for :class:`~walter.config.Config`, particularly the :meth:`~walter.config.Config.__call__` method.

Setting your configuration
-----

Walter currently loads your settings from the following places, listed in the order Walter checks them:

- Environment variables.
- A ``settings.ini`` file in the following locations:

    - The current working directory.
    - The user data directory (usually ``/home/<username>/.local/share/<appname>`` on Linux, ``/Users/<username>/Library/Application Support/<appname>`` on macOS, ``C:\Users\<username>\AppData\Local\<appauthor>\<appname>`` on Windows).
    - The site data directory (usually ``/usr/local/share/<appname>`` on Linux, ``/Library/Application Support/<appname>`` on macOS).

When loading settings from an INI file, Walter expects them to be under a ``[settings]`` heading, like so:

.. code-block:: ini

    [settings]
    DATABASE_URL=postgres://localhost/myapp

You can customise most aspects of how this loading happens; take a look at the :doc:`api` documentation for details.
