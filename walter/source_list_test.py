from contextlib import contextmanager
from pathlib import Path
from tempfile import TemporaryDirectory

import pytest

from .source_list import SourceList

DIR = object()


@contextmanager
def temp_dir_structure(structure: dict):
    # TODO: turn this into a proper pytest fixture thingy.
    with TemporaryDirectory() as p_str:
        p = Path(p_str)
        for name, contents in structure.items():
            path = p / name
            if contents is DIR:
                path.mkdir(parents=True, exist_ok=True)
            else:
                path.parent.mkdir(parents=True, exist_ok=True)
                mode = 'wb' if isinstance(contents, bytes) else 'w'
                with path.open(mode) as f:
                    f.write(contents)
                    f.flush()
                    print(contents)
        try:
            yield p
        finally:
            pass  # tempdir will get destroyed by the TemporaryDirectory CM


def test_source_list_normal(monkeypatch):
    monkeypatch.setenv('FOO', 'bar')
    s = {'settings.ini': "[settings]\nBAZ: qux\n"}
    with temp_dir_structure(s) as p:
        source_list = SourceList(search_path=[str(p)])
    assert source_list['FOO'] == 'bar'
    assert source_list['BAZ'] == 'qux'
    with pytest.raises(KeyError):
        source_list['EGGS']
