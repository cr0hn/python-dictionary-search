from typing import Tuple, Set, List


def _search(current, target, path) -> Tuple[str, object]:
    if isinstance(current, dict):
        if target in current:
            yield (*path, target), current[target]

        for x, y in current.items():
            for res in _search(y, target, (*path, x)):
                yield res
    elif isinstance(current, list):
        for i, item in enumerate(current):
            for res in _search(item, target, (*path, f"[{i}]")):
                yield res


def search_first(tree: dict,
                 target: str,
                 ancestors: Set[str] = None,
                 path_as_string: bool = True) -> Tuple[str, str]:
    ancestors = ancestors or set([])

    for (path, element) in _search(tree, target, tuple()):
        if ancestors <= set(path):

            if path_as_string:
                _path = ".".join(path)
            else:
                _path = path

            return _path, element


def search_all(tree: dict,
               target: str,
               ancestors: Set[str] = None,
               path_as_string: bool = True) -> List[Tuple[str, str]]:
    ancestors = ancestors or set([])

    res = list()

    for (path, element) in _search(tree, target, tuple()):
        if ancestors <= set(path):
            if path_as_string:
                _path = ".".join(path)
            else:
                _path = path

            res.append((_path, element))

    return res

__all__ = ["search_first", "search_all"]
