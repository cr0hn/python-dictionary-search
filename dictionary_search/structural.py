from typing import Iterable, List, Any, Tuple
from functools import singledispatch, reduce


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
    if len(l) == 0:
        yield current, l
        return  
    for i, v in enumerate(l):
        nc = __next_current(current, f"[{i}]")
        yield from flat(v, nc)


def __part_type(part: str) -> str | int:
    if part.startswith("[") and part.endswith("]"):
        return int(part[1:-1])
    return part


# TODO: please structural pattern matching this
def __nest_recursion(data, part_value):
    parts, value = part_value
    if isinstance(parts, list) and len(parts) == 1:
        if isinstance(parts[0], int):
            if len(data) == 0:
                data = []
            if len(data) <= parts[0]:
                data.extend([None] * (parts[0] - len(data) + 1))
        data[parts[0]] = value
    elif isinstance(parts, list) and isinstance(parts[0], str):
        if parts[0] not in data:
            data[parts[0]] = {}
        data[parts[0]] = __nest_recursion(data[parts[0]], (parts[1:], value))
    elif isinstance(parts[0], int):
        if len(data) == 0:
            data = []
        if len(data) <= parts[0]:
            data.extend([None] * (parts[0] - len(data) + 1))
        data[parts[0]] = __nest_recursion(data[parts[0]], (parts[1:], value))
    else:
        raise NotImplementedError
    return data


def nest(items: List[Tuple[str, Any]]): 
    keys = [x for x, _ in items]
    level_parts = [[__part_type(p) for p in x.split(".")] for x in keys]
    values = [x for _, x in items]

    # type check
    types = set(map(type, [x[0] for x in level_parts]))
    if len(types) > 1:
        raise ValueError("Cannot nest mixed types")
    level_type = types.pop()
    type_values = list(zip(level_parts, values))

    if level_type == str:
        return reduce(__nest_recursion, type_values, {})
    elif level_type == int:
        return reduce(__nest_recursion, type_values, [])
    raise NotImplementedError


__all__ = ["flat", "nest"]
