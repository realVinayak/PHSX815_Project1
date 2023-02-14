import numpy as np
import math
from file_list_utils import write_list

# Definitions for experiments. Exported to other files
MEAN_1 = 2
MEAN_2 = 3
SIGMA = 1
N_measurements = 20
N_samples = 1000000
ALPHA = 0.95
BETA = 10 ** (-3)


def generate_data(n_measurements, n_samples, mean_1, mean_2, sigma, first=True):
    raw_measurements = np.random.normal(mean_1 if first else mean_2,
                                        sigma/math.sqrt(n_measurements),
                                        n_samples)
    file_name = f'./outputs/rawdraw_{0 if first else 1}.txt'
    write_list(raw_measurements, file_name)
    print('written raw measurements to', file_name)


if __name__ == '__main__':
    generate_data(N_measurements, N_samples, MEAN_1, MEAN_2, SIGMA)
    generate_data(N_measurements, N_samples, MEAN_1, MEAN_2, SIGMA, False)


