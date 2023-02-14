from file_list_utils import write_multi_list
from analyze_data import get_analyzed_data
from generate_data import MEAN_1, MEAN_2, N_experiments, N_measurements, \
    SIGMA_RANGE, \
    ALPHA, BETA


# Gets minimum number of measurements for a fixed sigma needed to get false
# negative rate below fnr_threshold. Increments by 3 each iteration to speed
# up process
def get_min_n_from_fnr(mean_1, mean_2, sigma, n_experiments, alpha,
                       fnr_threshold):
    n_measurements = 1
    while \
    get_analyzed_data(mean_1, mean_2, sigma, n_measurements, n_experiments,
                      alpha,
                      read_from_file=False)[-1] > fnr_threshold:
        n_measurements += 3
    return n_measurements


# Gets minimum number of measurements for each sigma in sigma_range (applies
# get_min_n_from_fnr) to each sigma in sigma_range
def get_min_n_variation(mean_1, mean_2, n_experiments, alpha, fnr_threshold,
                        sigma_range):
    min_n_variation = []
    for sigma in sigma_range:
        min_n = get_min_n_from_fnr(mean_1, mean_2, sigma, n_experiments, alpha,
                                   fnr_threshold)
        print('min n = ', min_n, 'for sigma = ', sigma)
        min_n_variation.append([min_n, sigma])
    write_multi_list(min_n_variation, './outputs/n_sigma_variation.txt')
    return min_n_variation


def write_min_n_variation_driver():
    get_min_n_variation(MEAN_1, MEAN_2, N_experiments, ALPHA, BETA, SIGMA_RANGE)


if __name__ == '__main__':
    write_min_n_variation_driver()
