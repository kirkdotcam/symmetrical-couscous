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

def subtractor(a: Union[int, float], b: Union[int, float]):
    """
        Function subtracts values from args a and b^2
    """
    return a-(b*b)

def square(a: Union[int, float]):
    """
        Function squares value from arg a
    """
    return a*a

def cube(a: Union[int, float]):
    """
        Function cubes value from arg a
    """
    return a*a*a

def power(a: Union[int, float], b: Union[int, float]):
    """
        Function raises value from arg a to the power of b
    """
    return a**b

def absolute(a: Union[int, float]):
    """
        Function returns absolute value of value from arg a
    """
    return abs(a)

def square_root(a: Union[int, float]):
    """
        Function returns square root of value from arg a
    """
    return a**(1/2)

def cube_root(a: Union[int, float]):
    """
        Function returns cube root of value from arg a
    """
    return a**(1/3)

def power_root(a: Union[int, float], b: Union[int, float]):
    """
        Function returns value from arg a to the power of b
    """
    return a**(1/b)

def factorial(a: Union[int, float]):
    """
        Function returns factorial of value from arg a
    """
    if a == 0:
        return 1
    else:
        return a*factorial(a-1)