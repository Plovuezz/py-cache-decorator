from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    _cache_dict = {}

    @wraps(func)
    def wrapper(*args: tuple) -> int:
        if func.__name__ in _cache_dict:
            if args in _cache_dict[func.__name__]:
                print("Getting from cache")
                return _cache_dict[func.__name__][args]

        for arg in args:
            if not isinstance(arg, (int, float, bool, str, tuple)):
                return func(*args)

        print("Calculating new result")
        result = func(*args)

        if func.__name__ not in _cache_dict:
            _cache_dict[func.__name__] = {}

        _cache_dict[func.__name__][args] = result

        return result
    return wrapper
