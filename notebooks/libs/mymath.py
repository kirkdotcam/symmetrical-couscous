from typing import Union

def adder(a: Union[int, float], b: Union[int, float]):
    """
        Function adds values from args a and b^2
    """
    return a+(b*b)

def multiplier(a: Union[int, float], b: Union[int, float]):
    """
        Function multiplies values from args a and b^2
    """
    return a*(b*b)

def divider(a: Union[int, float], b: Union[int, float]):
    """
        Function divides values from args a and b^2
    """
    return a/(b*b)

def integral(a,b):
    return "Dont to integrals, they're hard."