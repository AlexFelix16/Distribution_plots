from scipy.stats import hypergeom
import matplotlib.pyplot as plt
import pandas as pd
import time


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


def hypergeom_graph(n, m, x):
    """ Calculates the distribituion of the number of mutations per DNA
    molecule for a give mutation rate

    Parameters
    ----------
    n : population size
    m : number of draws
    x : number of objects in the successful population

    Returns
    -------
    Graph containing a hypergeometric distribution with the given parameters

    """

    # Time the function
    start_time = time.time()

    # defining list of x values, nucleotides 1 to n
    x_values = list(range(x+1))
    # The probability of having i number of mutations per molecule
    dist = [hypergeom.pmf(i, n, m, x) for i in x_values]
    # Choosing a size for the graph
    plt.figure(figsize=(3.5, 2))
    # X-axis is the r_values, while y axis is their probabilities
    plt.bar(x_values, dist,
            align='center', edgecolor='black', color='blue')
    plt.xlabel('Number of copies in sample')
    plt.ylabel('Probability of')
    plt.grid(color='black', linestyle='--', linewidth=0.2, axis="y")
    # title = ('Mut dist at ' + str(100*p) + '% mut rate for ' + str(n) + " nt long seq")
    # plt.title(title)
    plt.tight_layout()
    # Save the file with the following name. The float_to_string function gets rides of decimals in the filename.
    filename = ('Probability of Number of copies in sample for n='
                + float_to_string(n) + ' m=' + float_to_string(m) + ' x=' + float_to_string(x))
    plt.savefig(filename, dpi=400, transparent=True, bbox_inches='tight')

    end_time = time.time()

    # total time taken
    print("Execution time of the program is", end_time - start_time, "sec.")

    # Saves the calculated distribution into a .csv file with the same filename as the plot
    table = pd.DataFrame(list(zip(x_values, dist)),
                         columns=['Copies', 'Probability'])

    table.to_csv(filename + '.csv', index=False)

hypergeom_graph(100, 25, 5)
