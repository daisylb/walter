API
===

Config
------

.. autoclass:: walter.config.Config
    :members:

Sources
-------

Built-In
::::::::

.. autoclass:: walter.sources.EnvironmentSource

.. autoclass:: walter.sources.IniFileSource

Creating your own sources
:::::::::::::::::::::::::

.. autoclass:: walter.sources.Source
    :members:

.. autoclass:: walter.sources.FileSource
    :members:

The ``NA`` object
-----

.. data:: walter.na.NA

    A singleton object representing an unavailable value, of type :class:`~walter.na.NaType`.

    Used to allow execution to continue when a value is unset or invalid, so that Walter can discover the remaining values.

.. autoclass:: walter.na.NaType
