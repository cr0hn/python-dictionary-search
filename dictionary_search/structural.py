from typing import Iterable
from functools import singledispatch


def __next_current(current: str, n: str):
    if current != "":
        return f"{current}.{n}"
    return n

@singledispatch
def flat(value, current: str = "") -> Iterable[tuple]:
    yield current, value


@flat.register(dict)
def _(d: dict, current: str = "") -> Iterable[tuple]:
    for k, v in d.items():
        nc = __next_current(current, k)
        yield from flat(v, nc)


@flat.register(list)
def _(l: list, current: str = "") -> Iterable[tuple]:
    for i, v in enumerate(l):
        nc = __next_current(current, f"[{i}]")
        yield from flat(v, nc)


__all__ = ["flat"]
