from dictionary_search import search_first

def test_search_one():
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

    res = search_first(d, "c")

    assert res[0] == "a.b.c"
    assert res[1] == "C value 1"

