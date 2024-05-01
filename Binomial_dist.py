from scipy.stats import binom
import matplotlib.pyplot as plt

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

def mut_graph(n, p, x):
    """ Calculates the distribituion of the number of mutations per DNA
    molecule for a give mutation rate

    Parameters
    ----------
    n : length of DNA in bps
    p : mutation rate in decimal (max value is 1)
    x : max value in x axis for the generated graph

    Returns
    -------
    Graph containing the mutation distribution

    """

    # defining list of r values, nucleotides 1 to n
    r_values = list(range(x + 1))
    # The probability of having r number of mutations per molecule
    dist = [binom.pmf(r, n, p) for r in r_values]

    # Choosing a size for the graph
    plt.figure(figsize=(3.5, 2))
    # X axis is the r_values, while y axis is their probabilities
    plt.bar(r_values[0:x], dist[0:x],
            align='center', edgecolor='black', color='blue')
    plt.xlabel('# of Mutations per RNA Molecule')
    plt.ylabel('Fraction')
    plt.grid(color='black', linestyle='--', linewidth=0.2, axis="y")
    title = ('Mut dist at ' + str(round((100*p),3))+ '% mut rate for ' + str(n) + " nt long seq")
    plt.title(title)
    plt.tight_layout()
    filename = 'Error dist at ' + float_to_string(p) + ' percent mut rate for 450 nt long DNA'
    plt.savefig(fname = filename, dpi=300, transparent=True, bbox_inches='tight')
    print(dist)


mut_graph(100, 0.03, 10)