import math

import numpy as np
import matplotlib.pyplot as plt
from file_list_utils import read_list

from generate_data import MEAN_1, MEAN_2, SIGMA, N_measurements, N_samples, \
    ALPHA

from histogram_utils import get_histogram_data


# Returns pdf at probe_value for a Gaussian with given mean and sigma
def get_gaussian_probability(probe_value, mean, sigma):
    normalizing_factor = (1 / math.sqrt(2 * math.pi * (sigma ** 2)))
    return normalizing_factor * (
        math.exp(-((probe_value - mean) ** 2) / (2 * (sigma ** 2))))


# Returns log likelihood ratio given callbacks for first probability and
# second probability and measurement
def get_log_likelihood_ratio(measurement, get_first_prob, get_second_prob):
    log_likelihood_ratio = math.log(
        get_first_prob(measurement) / get_second_prob(
            measurement))
    return log_likelihood_ratio


# Returns LLR for all experiments. Reads from output file from generate_data.py
def get_llr_distribution(n_measurements, mean_1, mean_2, sigma,
                         first=True):
    file_name = f'./outputs/rawdraw_{0 if first else 1}.txt'
    load_raw = read_list(file_name)
    llr_ratios = [get_log_likelihood_ratio(measurement,
                                           lambda
                                               value: get_gaussian_probability(
                                               value, mean_2,
                                               sigma / math.sqrt(
                                                   n_measurements)),
                                           lambda
                                               value: get_gaussian_probability(
                                               value, mean_1,
                                               sigma / math.sqrt(
                                                   n_measurements)))
                  for
                  measurement in load_raw]
    llr_ratios.sort()
    return llr_ratios


# Returns false negative rate given llr measurements and lambda threshold
def get_fnr(llr_measurements, lambda_threshold):
    llr_passed_count = 0
    for llr in llr_measurements:
        if llr > lambda_threshold:
            break
        llr_passed_count += 1
    return llr_passed_count / len(llr_measurements)


# Analyzes data by calculating false negative rate
def get_analyzed_data(mean_1, mean_2, sigma, n_measurements, alpha):
    _hypothesis_1_llr = get_llr_distribution(n_measurements, mean_1, mean_2,
                                             sigma)
    _lambda_alpha = np.percentile(_hypothesis_1_llr, 100 * alpha)
    _hypothesis_2_llr = get_llr_distribution(n_measurements, mean_1, mean_2,
                                             sigma, False)
    _fnr = get_fnr(_hypothesis_2_llr, _lambda_alpha)
    return _hypothesis_1_llr, _hypothesis_2_llr, _lambda_alpha, _fnr


def plot_hypothesis():
    hypothesis_1_llr, hypothesis_2_llr, lambda_alpha, fnr = get_analyzed_data(
        MEAN_1, MEAN_2, SIGMA, N_measurements, ALPHA)

    hypothesis_1_probs, hypothesis_1_bins = get_histogram_data(hypothesis_1_llr,
                                                               N_samples + 1)
    hypothesis_2_probs, hypothesis_2_bins = get_histogram_data(hypothesis_2_llr,
                                                               N_samples + 1)

    print('false negative rate: ', fnr)

    # Workaround for adding colored legends
    plt.plot([], 'r')
    plt.plot([], 'g')

    plt.plot(hypothesis_1_bins, hypothesis_1_probs, 'r--', linewidth=0.3,
             alpha=0.4)
    plt.vlines(lambda_alpha, 0,
               max(max(hypothesis_1_probs), max(hypothesis_2_probs)),
               color='black', linewidth=1)
    plt.plot(hypothesis_2_bins, hypothesis_2_probs, 'g--', linewidth=0.3,
             alpha=0.5)

    plt.xlabel('\u03BB = L(H2)/L(H1)')
    plt.ylabel('Probability')
    plt.title(f'{N_measurements} number of measurements')
    plt.legend(['P(\u03BB|H1)', 'P(\u03BB|H2)'])
    plt.savefig('./outputs/analyzed_data.png')


if __name__ == '__main__':
    plot_hypothesis()