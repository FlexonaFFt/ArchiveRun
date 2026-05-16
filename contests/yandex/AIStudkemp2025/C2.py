import sys
from functools import wraps

# WA: test 5
def takes(*types):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if len(args) < len(types):
                raise TypeError("Not enough arguments")

            for i, (arg, type_) in enumerate(zip(args, types)):
                if not isinstance(arg, type_):
                    raise TypeError(f"Argument {i} is not of type {type_}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

if __name__ == "__main__":
    exec(sys.stdin.read())
