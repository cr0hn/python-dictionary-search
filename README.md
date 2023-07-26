# Dictionary Search tools

![License](https://img.shields.io/badge/License-Apache2-SUCCESS)
![Pypi](https://img.shields.io/pypi/v/dictionary-search)
![Python Versions](https://img.shields.io/badge/Python-3.8%20%7C%203.9%20%7C%203.10-blue)

In a nutshell ``Dictionary Search`` is a small library to search in a dictionaries recursively.
Also have some other dictionary tools to make your life easier.

# Install

```bash
> pip install dictionary-search
```

# Search

```python
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
print()
print("Search First (path as tuple): ", search_first(d, "c", path_as_string=False))
print("Search All (path as tuple): ", search_all(d, "c", path_as_string=False))

```

After running the code, you will see:

```bash
> python examples/example.py
Search First:  ('a.b.c', 'C value 1')
Search All:  [('a.b.c', 'C value 1'), ('h.c', 'C value 2')]

Search First (path as tuple):  (('a', 'b', 'c'), 'C value 1')
Search All (path as tuple):  [(('a', 'b', 'c'), 'C value 1'), (('h', 'c'), 'C value 2')]
```

# Flat and Nest

Allow you to flat and rebuild a dict. Nest only work with str and index keys.

```python
data = {"a": {"b": 1, "c": 2}}
flat_data = flat(data) # will produce: [("a.b", 1), ("a.c", 2)]
assert data == nest(flat_data)
```

> TODO: describe list

If you want more information, please take a look to our test


# Authors

- [Cesar Gallego](https://github.com/CesarGallego)
- [cr0hn](https://github.com/cr0hn)

# License

Dictionary Search is Open Source and available under the [MIT](https://github.com/cr0hn/python-dictionary-search/blob/main/LICENSE).

# Contributions

Contributions are very welcome. See [CONTRIBUTING.md](https://github.com/cr0hn/python-dictionary-search/blob/main/CONTRIBUTING.md>) or skim existing tickets to see where you could help out.


