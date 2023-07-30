import pytest

from dictionary_search import nest


def test_mixing_types():
    with pytest.raises(ValueError):
        d = [("a", 1), ("[0]", 2)]
        nest(d)


def test_simple_nest():
    base = {"a": 1, "b": 2}
    d = list({"a": 1, "b": 2}.items())
    assert nest(d) == base 


def test_nest_prop():
    d = list({"a.b": 1, "a.c": 2}.items())
    assert nest(d) == {"a": {"b": 1, "c": 2}}


def test_mixed_nesting():
    d = list({"a.b": 1, "a.c": 2, "d": 3}.items())
    assert nest(d) == {"a": {"b": 1, "c": 2}, "d": 3}


def test_list_nesting():
    d = [("a.b", 1), ("a.c", 2), ("d", 3)]
    assert nest(d) == {"a": {"b": 1, "c": 2}, "d": 3}


def test_index_nesting():
    d = [("[0]", 1), ("[1]", 2), ("[2]", 3)]
    assert nest(d) == [1, 2, 3]


def test_empty_list_nested():
    d = [('_meta.operators', [])]

    assert nest(d) == {'_meta': {'operators': []}}
