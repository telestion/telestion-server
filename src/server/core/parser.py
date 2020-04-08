from abc import ABC, abstractmethod


class ValidatorAnswer:
    """Class that is_valid function in Parser should return."""

    def __init__(self, code=None, error=None):
        self.code = code
        self.error = error

    def __bool__(self):
        return self.error is None


class Parser(ABC):
    """Interface to build parser for api parts."""

    def __init__(self, args, **kwargs):
        self.args = args
        for k, v in kwargs.items():
            self.args[k] = v

    def __getattr__(self, item):
        return self.args.get(item, None)

    @abstractmethod
    def is_valid(self) -> ValidatorAnswer:
        pass
