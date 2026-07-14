import pytest

from bukuserver.filters import (
    equal_func, not_equal_func, contains_func, not_contains_func,
    greater_func, smaller_func, in_list_func, not_in_list_func,
    top_x_func, bottom_x_func, TagBaseFilter,
)


QUERY = [
    (1, 'alpha', 5),
    (2, 'beta', 10),
    (3, 'gamma', 15),
    (4, 'delta', 20),
]


def test_not_equal_func():
    result = list(not_equal_func(QUERY, 'beta', 1))
    assert (2, 'beta', 10) not in result
    assert len(result) == 3


def test_contains_func():
    result = list(contains_func(QUERY, 'am', 1))
    assert result == [(3, 'gamma', 15)]


def test_not_contains_func():
    result = list(not_contains_func(QUERY, 'am', 1))
    assert (3, 'gamma', 15) not in result
    assert len(result) == 3


def test_greater_func():
    result = list(greater_func(QUERY, 10, 2))
    assert result == [(3, 'gamma', 15), (4, 'delta', 20)]


def test_smaller_func():
    result = list(smaller_func(QUERY, 10, 2))
    assert result == [(1, 'alpha', 5)]


def test_in_list_func():
    result = list(in_list_func(QUERY, ['alpha', 'delta'], 1))
    assert result == [(1, 'alpha', 5), (4, 'delta', 20)]


def test_not_in_list_func():
    result = list(not_in_list_func(QUERY, ['alpha', 'delta'], 1))
    assert result == [(2, 'beta', 10), (3, 'gamma', 15)]


def test_top_x_func():
    result = list(top_x_func(QUERY, 2, 2))
    values = sorted(item[2] for item in result)
    assert values == [15, 20]


def test_bottom_x_func():
    result = list(bottom_x_func(QUERY, 2, 2))
    values = sorted(item[2] for item in result)
    assert values == [5, 10]


def test_tagbasefilter_invalid_name_raises():
    with pytest.raises(ValueError):
        TagBaseFilter(name='invalid_name')
