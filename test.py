from scipy.stats import hypergeom
import time

m = 10**12
n = 10
x = m/4

start_time = time.time()
test = hypergeom.pmf(0 ,m, n, x)
end_time = time.time()

# total time taken
print("Execution time of the program is", end_time - start_time, "sec.")
print(test)

def test_plot(x,y):
    plt.figure(figsize=(3.5, 2))
    # X-axis is the r_values, while y axis is their probabilities
    x_axis=len(x)
    y_axis=len(y)
    plt.bar(x, y, align='center', edgecolor='black', color='blue')
    plt.xlabel('Number of copies in sample')
    plt.ylabel('Probability of')
    plt.grid(color='black', linestyle='--', linewidth=0.2, axis="y")
    # title = ('Mut dist at ' + str(100*p) + '% mut rate for ' + str(n) + " nt long seq")
    # plt.title(title)
    plt.tight_layout()
    filename = ('Probability of Number of copies in sample for n=' + str(n) + ' m=' + str(m) + ' x=' + str(x))
    plt.savefig(filename, dpi=400, transparent=True, bbox_inches='tight')