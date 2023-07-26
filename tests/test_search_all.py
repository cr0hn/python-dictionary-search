from dictionary_search import search_all


def test_search_all():
    d = {
        "a": {
            "b": {
                "c": "C value 1"
            }
        },
        "e": "f",
        "h": [
            {
                "i": "j"
            },
            {
                "c": "C value 2"
            }
        ]
    }


    res = search_all(d, "c")

    assert res[0][0] == "a.b.c"
    assert res[0][1] == "C value 1"
    assert res[1][0] == "h.[1].c"
    assert res[1][1] == "C value 2"
