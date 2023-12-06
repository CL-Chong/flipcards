# import functools
# from typing import Any


def is_dunder(name: str):
    return name.startswith("__") and name.endswith("__")


class QuestionBank(type):
    def __new__(mcs, name, bases, attrs, **kwds):
        attrs["dispatcher"] = {
            key: qfun
            for key, qfun in attrs.items()
            if callable(qfun) and not is_dunder(key)
        }

        return super().__new__(mcs, name, bases, attrs)
