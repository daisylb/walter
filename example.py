from walter.config import Config

with Config("ACME", "Widget") as config:
    some_config = config("FOO")
    other_config = config("BAR", cast=int)
