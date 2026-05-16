import sys
from functools import wraps

def takes(*types):
    def decorator(func):
        @wraps(func)
        def wrapper(*args):
            for i, (arg, expected_type) in enumerate(zip(args, types)):
                if not isinstance(arg, expected_type):
                    raise TypeError
            return func(*args)
        return wrapper
    return decorator

exec(sys.stdin.read())
