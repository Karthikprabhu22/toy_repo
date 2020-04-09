import random
from matplotlib import pyplot as plt

# Function to convert a given decimal number to a ternary
def ter(n):
    ans = ""
    while n > 0:
        dig = int(n%3)
        ans += str(dig)
        n //= 3
    ans = ans[::-1]  #To reverse the string
    return ans


def random_string(length):
    '''
    Returns a random bit string of the given length.

    Parameters
    ----------
    length: int
        Posivite integer that specifies the desired length of the bit string.

    Returns
    -------
    out: list
        The random bit string given as a list, with int elements.
    '''
    if not isinstance(length, int) or length < 0:
        raise ValueError("input length must be a positive ingeter")
    return [random.randint(0,1) for _ in range(length)]

def lookup_table(rule_number):
    '''
    Returns a dictionary which maps ECA neighborhoods to output values.
    Uses Wolfram rule number convention.

    Parameters
    ----------
    rule_number: int
        Integer value between 0 and 19682, inclusive. Specifies the ECA lookup table
        according to the Wolfram numbering scheme.

    Returns
    -------
    lookup_table: dict
        Lookup table dictionary that maps neighborhood tuples to their output according to the
        ECA local evolution rule (i.e. the lookup table), as specified by the rule number.
    '''
    if not isinstance(rule_number, int) or rule_number < 0 or rule_number > 19682:
        raise ValueError("rule_number must be an int between 0 and 19682, inclusive")
    neighborhoods = [(0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2)]
    in_ternary = '{:{fill}{align}{width}}'.format(ter(rule_number),
                                                  fill='0',
                                                  align='>',
                                                  width='9')

    return dict(zip(neighborhoods, map(int,reversed(in_ternary)))) # use map so that outputs are ints, not strings

def spacetime_diagram(spacetime_field, size=12, colors=plt.cm.Greys):
    '''
    Produces a simple spacetime diagram image using matplotlib imshow with 'nearest' interpolation.

   Parameters
    ---------
    spacetime_field: array-like (2D)
        1+1 dimensional spacetime field, given as a 2D array or list of lists. Time should be dimension 0;
        so that spacetime_field[t] is the spatial configuration at time t.

    size: int, optional (default=12)
        Sets the size of the figure: figsize=(size,size)
    colors: matplotlib colormap, optional (default=plt.cm.Greys)
        See https://matplotlib.org/tutorials/colors/colormaps.html for colormap choices.
        A colormap 'cmap' is called as: colors=plt.cm.cmap
    '''
    plt.figure(figsize=(size,size))
    plt.imshow(spacetime_field, cmap=colors, interpolation='nearest')
    plt.show()
