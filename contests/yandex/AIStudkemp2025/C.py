import sys
from functools import wraps

def takes(*types):
    def decorator(func):
        @wraps(func)
        def wrapper(*args):
            for i, (arg, expected_type) in enumerate(zip(args, types)):
                if not isinstance(arg, expected_type):
                    raise TypeError(f"Argument {i} is of type {type(arg).__name__}, expected {expected_type.__name__}")
                return func(*args)
            return wrapper
        return decorator


if __name__ == '__main__':
    exec(sys.stdin.read())
