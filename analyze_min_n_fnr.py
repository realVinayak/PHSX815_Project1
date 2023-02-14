from file_list_utils import read_multi_list
import matplotlib.pyplot as plt


# Plots relationship between minimum number of measurements and standard
# deviation to get false negative rate below threshold
def n_std_variation_plot_driver():
    n_std_variation = read_multi_list('./outputs/n_sigma_variation.txt')
    std_list = [x[1] for x in n_std_variation]
    n_list = [x[0] for x in n_std_variation]
    plt.plot(std_list, n_list, '--bo')
    plt.xlabel('Standard Deviation \u03C3')
    plt.ylabel('Number of Measurements')
    plt.title('\u03B2 = 10\u207B\u00B3')
    plt.savefig('./outputs/n_sigma_variation.png')
    plt.show()


if __name__ == '__main__':
    n_std_variation_plot_driver()
