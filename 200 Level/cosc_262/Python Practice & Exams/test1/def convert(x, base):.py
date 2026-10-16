def convert(x, base):

    # Check for not an integer
    if not isinstance(x, int):
        raise TypeError ("x is not an integer")
    if not isinstance(base, int):
        raise TypeError ("base is not an integer")

    
    # Check for not positive x or greater than 2 base
    if x < 0:
        raise ValueError("x must be positive")
    if base < 2:
        raise ValueError("base cannot be less than 2")

    # Create an empty list for the output and set our iterable variable to n
    out = []
    n = x

    # Loop over n, and add the remainder to out
    while n > 0:
        # Remainder of n mod base --> e.g (1234 mod 10 = 123 * 10 + 4)
        remainder = n % base

        # Add the difference to the output list
        out.append(remainder)
        
        # Devide n by the base to iterate over
        n = n // base
    out.reverse()
    return out

print(convert(1234, 10))