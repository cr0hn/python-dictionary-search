from dictionary_search.structural import flat


def test_simple_dict():
    d = {"a": 1, "b": 2, "c": 3}

    res = list(flat(d))

    assert res == [("a", 1), ("b", 2), ("c", 3)]


def test_nested_dict():
    d = {"a": 1, "b": {"c": 2, "d": 3}}

    res = list(flat(d))

    assert res == [("a", 1), ("b.c", 2), ("b.d", 3)]


def test_simple_list():
    l = [1, 2, 3]

    res = list(flat(l))

    assert res == [("[0]", 1), ("[1]", 2), ("[2]", 3)]


def test_nested_empty_list():
    l = {"a": {"b": []}}

    res = list(flat(l))

    assert res == [("a.b", [])]

def test_nested_list():
    l = [1, [2, 3]]

    res = list(flat(l))

    assert res == [("[0]", 1), ("[1].[0]", 2), ("[1].[1]", 3)]


def test_nested_list_and_dict():
    l = [1, {"a": 2, "b": 3}]

    res = list(flat(l))

    assert res == [("[0]", 1), ("[1].a", 2), ("[1].b", 3)]


def test_nested_dict_and_list():
    d = {"a": 1, "b": [2, 3]}

    res = list(flat(d))

    assert res == [("a", 1), ("b.[0]", 2), ("b.[1]", 3)]


def test_nested_dict_and_list_and_dict():
    d = {"a": 1, "b": [2, {"c": 3, "d": 4}]}

    res = list(flat(d))

    assert res == [("a", 1), ("b.[0]", 2), ("b.[1].c", 3), ("b.[1].d", 4)]
