from walter.config import Config

with Config('ACME', 'Widget') as config:
    some_config = config.get('FOO')
    other_config = config.get('BAR', cast=int)
