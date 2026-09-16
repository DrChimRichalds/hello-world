def handleNonIntArguments(func):
    def wrapper(*args):
        try:
            for arg in args:
                if not isinstance(arg, int):
                    raise NonIntArgumentException
            func(*args)
        except TypeError:
            print('type error occurred')
        except Exception: 
            print('Some other exception')

    return wrapper


class NonIntArgumentException(Exception):
    def __init__(self):
        print('NonIntArgumentException: All arguments must be integers')

@handleNonIntArguments
def sum(a, b, c):
    print(a+b+c)
    return a + b + c

sum(1,2,'a')

