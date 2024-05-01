
def float_to_string(num):
    """
    Convert a float number to a string, replacing the decimal point with the word "point". This simplifies
    automatically generating file names for the figures

    Parameters:
    num (float): The float number to convert.

    Returns:
    str: The converted string.
    """
    # Check if the number is an integer
    if num.is_integer():
        return str(int(num))

    # Split the float into its integer and decimal parts
    integer, decimal = str(num).split('.')

    # Return a string with the word "point" in between
    return integer + " point " + decimal

print(float_to_string(9))