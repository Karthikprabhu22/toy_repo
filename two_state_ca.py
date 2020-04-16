import random
from matplotlib import pyplot as plt


def decimal_to_ternary(rule_in_decimal):
    """
    Function to convert a given decimal number to a ternary

    Parameters
    ----------
    rule_in_decimal: int
        Posivite integer that specifies the decimal number.

    Returns
    -------
    rule_in_ternary: int
        The ternary representation of the input number.
    """
    rule_in_ternary = ""
    while rule_in_decimal > 0:
        remainder = int(rule_in_decimal % 3)
        rule_in_ternary += str(remainder)
        rule_in_decimal //= 3
    rule_in_ternary = rule_in_ternary[::-1]
    return rule_in_ternary


def random_string(length):
    """
    Returns a random bit string of the given length.

    Parameters
    ----------
    length: int
        Posivite integer that specifies the desired length of the bit string.

    Returns
    -------
    out: list
        The random bit string given as a list, with int elements.
    """
    if not isinstance(length, int) or length < 0:
        raise ValueError("input length must be a positive ingeter")
    return [random.randint(0, 2) for _ in range(length)]


def lookup_table(rule):
    """
    Returns a dictionary which maps ECA neighborhoods to output values.
    Uses Wolfram rule number convention.

    Parameters
    ----------
    rule: int
        Integer value between 0 and 19682, inclusive. Specifies the ECA
        lookup table according to the Wolfram numbering scheme.

    Returns
    -------
    lookup_table: dict
        Lookup table dictionary that maps neighborhood tuples to their output
        according to the ECA local evolution rule (i.e. the lookup table),
        as specified by the rule number.
    """
    if not isinstance(rule, int) or rule < 0 or rule > 19682:
        raise ValueError("rule must be an int between 0 and 19682, inclusive")
    neighborhoods = [
        (0, 0),
        (0, 1),
        (0, 2),
        (1, 0),
        (1, 1),
        (1, 2),
        (2, 0),
        (2, 1),
        (2, 2),
    ]
    in_ternary = "{:{fill}{align}{width}}".format(
        decimal_to_ternary(rule), fill="0", align=">", width="9"
    )

    return dict(zip(neighborhoods, map(int, reversed(in_ternary))))


def spacetime_field(rule_number, initial_condition, time_steps):
    """
    Returns a spacetime field array using the given rule number on the
    given initial condition for the given number of time steps.

    Parameters
    ----------
    rule_number: int
        Integer value between 0 and 19682, inclusive. Specifies the ECA
        lookup table according to the Wolfram numbering scheme.
    initial_condition: list
        Binary string used as the initial condition for the ECA.
        Elements of the list should be ints.
    time_steps: int
        Positive integer specifying the number of time steps for
        evolving the ECA.
    """
    if time_steps < 0:
        raise ValueError("time_steps must be a non-negative integer")
    # try converting time_steps to int
    try:
        time_steps = int(time_steps)
    except ValueError:
        raise ValueError("time_steps must be a non-negative integer")

    for i in initial_condition:
        if i not in [0, 1, 2]:
            raise ValueError("initial condition must be a list of 0s and 1s")

    lookup = lookup_table(rule_number)
    length = len(initial_condition)

    # initialize spacetime field and current configuration
    spacetime_field = [initial_condition]
    current_configuration = initial_condition.copy()

    # apply the lookup table to evolve the CA for given number of time step
    for t in range(time_steps):
        new_configuration = []
        for i in range(length):

            neighborhood = (current_configuration[(i - 1)], current_configuration[i])

            new_configuration.append(lookup[neighborhood])

        current_configuration = new_configuration
        spacetime_field.append(new_configuration)

    return spacetime_field


def spacetime_diagram(spacetime_field, size=12, colors=plt.cm.Greys):
    """
    Produces a simple spacetime diagram image using matplotlib imshow with
    'nearest' interpolation.

   Parameters
    ---------
    spacetime_field: array-like (2D)
        1+1 dimensional spacetime field, given as a 2D array or list of lists.
        Time should be dimension 0; so that spacetime_field[t] is the spatial
        configuration at time t.

    size: int, optional (default=12)
        Sets the size of the figure: figsize=(size,size)
    colors: matplotlib colormap, optional (default=plt.cm.Greys)
        See https://matplotlib.org/tutorials/colors/colormaps.html for
        choices. A colormap 'cmap' is called as: colors=plt.cm.cmap
    """
    plt.figure(figsize=(size, size))
    plt.imshow(spacetime_field, cmap=colors, interpolation="nearest")
    plt.show()
