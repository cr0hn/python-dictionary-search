# File: example.py

from dictionary_search import search_first, search_all

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

print("Search First: ", search_first(d, "c"))
print("Search All: ", search_all(d, "c"))

print("Search First (path as tuple): ", search_first(d, "c", path_as_string=False))
print("Search All (path as tuple): ", search_all(d, "c", path_as_string=False))
