
def hypervolume(length, *lengths):
    """
    example of using variable params in a function 
    code example:
        >>> from examples import hypervolume
        >>> hypervolume(4,5,6)
            120
        >>> hypervolume()
            Traceback (most recent call last):
            File "<stdin>", line 1, in <module>
            TypeError: hypervolume() missing 1 required positional argument: 'length'
        >>> hypervolume(2,3,4,54,5)
            6480
        >>> exit()
    """
    v = length
    for item in lengths:
        v *= item
    return v

def tag(name, **attributes):
    """
    this is an example of using a variable number of named arguments
    code example:
        >>> from examples import tag
        >>> tag('img', src='monet.jpg', alt='sunrise by monet', border=1)
            '<img src = "monet.jpg" alt = "sunrise by monet" border = "1">'
        >>> exit()
    """
    result = '<' + name
    for key, value in attributes.items():
        result += ' {k}="{v}"'.format(k=key, v=str(value))
    result += '>'
    return result

def trace(f, *args, **kwargs):
    """
    example of forwarding arguments
    code example:
    >>> from examples import trace
    >>> int('ff', base=16)
        255
    >>> trace(int, 'ff', base=16)
        args =  ('ff',)
        kwargs =  {'base': 16}
        result =  255
        255
    """
    print('args = ', args)
    print('kwargs = ', kwargs)
    result = f(*args, **kwargs)
    print('result = ', result)
    return result

def sort_by_last_letter(strings):
    """
    example of a local scope function, or a local function.
    the function is defined inside of another function and can be called from inside that function
    code example:
        >>> from examples import sort_by_last_letter
        >>> sort_by_last_letter(['hello', 'from', 'a', 'local', 'function'])
        ['a', 'local', 'from', 'function', 'hello']
    """
    def last_letter(s):
        return s[-1]
    return sorted(strings, key=last_letter)

def raise_to(exp):
    """
    shows an example of a function factory
    also shows an example of a closure and how it wraps the variable in scope
    code example:
        >>> from examples import raise_to
        >>> square = raise_to(2)
        >>> square.__closure__
        (<cell at 0x103a7d618: int object at 0x1009e09a0>,)
        >>> square(5)
        25
        >>> square(1234)
        1522756
        >>> cube = raise_to(3)
        >>> cube(3)
        27
        >>> cube(10)
        1000
        >>> cube(23)
        12167
        >>>
    """
    def raise_to_exp(x):
        return pow(x,exp)
    return raise_to_exp