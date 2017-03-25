import pytest

from .na import NA


def test_repr():
    assert repr(NA) == "NA"


def test_str():
    assert str(NA) == "NA"


def test_bytes():
    assert bytes(NA) == b"NA"


def test_format():
    assert "{}".format(NA) == "NA"
    assert "{:x}".format(NA) == "NA"
    assert "{:02f}".format(NA) == "NA"
    assert "{: <}".format(NA) == "NA"
    assert "{:totally-invalid-fspec}".format(NA) == "NA"


def test_bool():
    assert not bool(NA)
    assert not NA


def test_float():
    assert float(NA) == 0.0


def test_complex():
    assert complex(NA) == 0 + 0j


def test_round():
    assert round(NA) == 0.0
    assert round(NA, 2) == 0.0


def test_call():
    assert NA() is NA
    assert NA(1, 2, 'eggs', 'spam') is NA
    assert NA(1, 2, foo='eggs', bar='spam') is NA


def test_attrs():
    assert NA.someattr is NA
    NA.foo = 1
    assert NA.foo is NA
    del NA.bar
    assert NA.bar is NA
    assert dir(NA) == []


def test_ordering():
    assert NA < 0
    assert 0 > NA
    assert NA < float('-inf')
    assert float('-inf') > NA
    assert NA <= 0
    assert 0 >= NA
    assert NA != 0
    assert 0 != NA
    assert NA != NA
    assert not NA == 0
    assert not 0 == NA
    assert not NA > 0
    assert not 0 < NA
    assert not NA >= 0
    assert not NA <= 0


def test_container():
    assert NA[1] is NA
    assert NA['foo'] is NA
    NA[1] = 1
    NA['foo'] = 'foo'
    assert NA[1] is NA
    assert NA['foo'] is NA
    del NA[1]
    del NA['foo']
    assert NA[1] is NA
    assert NA['foo'] is NA
    assert 1 not in NA
    assert 'foo' not in NA


def test_iter():
    assert len(list(iter(NA))) == 0
    assert len(list(reversed(NA))) == 0


def test_numeric_opers():
    assert NA + 1 is NA
    assert 1 + NA is NA
    assert NA - 1 is NA
    assert 1 - NA is NA
    assert NA * 1 is NA
    assert 1 * NA is NA
    assert NA @ 1 is NA
    assert 1 @ NA is NA
    assert NA / 1 is NA
    assert 1 / NA is NA
    assert NA // 1 is NA
    assert 1 // NA is NA
    assert NA % 1 is NA
    assert 1 % NA is NA
    assert NA ** 1 is NA
    assert 1 ** NA is NA
    assert NA << 1 is NA
    assert 1 << NA is NA
    assert NA >> 1 is NA
    assert 1 >> NA is NA
    assert NA & 1 is NA
    assert 1 & NA is NA
    assert NA ^ 1 is NA
    assert 1 ^ NA is NA
    assert NA | 1 is NA
    assert 1 | NA is NA
    assert -NA is NA
    assert +NA is NA
    assert abs(NA) is NA
    assert ~NA is NA


@pytest.mark.parametrize('left', (True, False))
def test_divmod(left):
    v = divmod(NA, 1) if left else divmod(1, NA)
    assert isinstance(v, tuple)
    assert len(v) == 2
    assert v[0] is NA
    assert v[1] is NA


def test_context_manager():
    y = None
    with NA as x:
        y = x
    assert y is NA


def test_context_manager_exc():
    with NA:
        raise ValueError('should not propagate')


@pytest.mark.asyncio
async def test_await():
    assert (await NA) is NA


@pytest.mark.asyncio
async def test_async_iter():
    n = 0
    async for _ in NA:  # noqa
        n += 1
    assert n == 0


@pytest.mark.asyncio
async def test_async_context_manager():
    y = None
    async with NA as x:
        y = x
    assert y is NA


@pytest.mark.asyncio
async def test_async_context_manager_exc():
    async with NA:
        raise ValueError('should not propagate')
