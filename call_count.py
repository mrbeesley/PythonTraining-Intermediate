"""
code example:
    >>> from call_count import hello
    >>> hello('michael')
        Hello, michael
    >>> hello('jason')
        Hello, jason
    >>> hello('andrew')
        Hello, andrew
    >>> hello('ryan')
        Hello, ryan
    >>> hello('jessica')
        Hello, jessica
    >>> hello.count
        5
"""

class CallCount:
    def __init__(self, f):
        self.f = f
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        return self.f(*args, **kwargs)

@CallCount
def hello(name):
    print('Hello, {}'.format(name))

