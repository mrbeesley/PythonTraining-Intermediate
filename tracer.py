"""
code example:
    >>> from tracer import rotate_list
    >>> l = [1,2,3]
    >>> l = rotate_list(l)
        Calling <function rotate_list at 0x1040a6620>
    >>> l
        [2, 3, 1]
    >>> l = rotate_list(l)
        Calling <function rotate_list at 0x1040a6620>
    >>> l
        [3, 1, 2]
    >>> l = rotate_list(l)
        Calling <function rotate_list at 0x1040a6620>
    >>> l
        [1, 2, 3]
    >>> from tracer import tracer
    >>> tracer.enabled = False
    >>> l = rotate_list(l)
    >>> l
        [2, 3, 1]
    >>> l = rotate_list(l)
    >>> l
        [3, 1, 2]
    >>> l = rotate_list(l)
    >>> l = rotate_list(l)
    >>> l
        [2, 3, 1]
"""

class Trace:
    def __init__(self):
        self.enabled = True

    def __call__(self, f):
        def wrap(*args, **kwargs):
            if self.enabled:
                print('Calling {}'.format(f))
            return f(*args, **kwargs)
        return wrap

tracer = Trace()

@tracer
def rotate_list(l):
    return l[1:] + [l[0]]
