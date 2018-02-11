"""
example of using a decorator to remove non-ascii character from a functions return value
code example: (without decorator)
    >>> from decoratorexample import northern_city
    >>> northern_city()
        'Tromsø'
    >>> exit()
code example: (with decorator)
    >>> from decoratorexample import northern_city
    >>> northern_city()
        "'Troms\\xf8'"
"""

def escape_unicode(f):
    def wrap(*args, **kwargs):
        x = f(*args, **kwargs)
        return ascii(x)
    return wrap

@escape_unicode
def northern_city():
    return 'Tromsø'