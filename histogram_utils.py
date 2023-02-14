import numpy as np


# Uses numpy's histogram generator and returns
# data that can be read efficiently by matplotlib
# Reason: matplotlib's histogram is slow. numpy's is fast.
def get_histogram_data(measurements, samples):
    temp_hist = list(np.histogram(measurements, samples, density=True))
    temp_hist_probs = list(temp_hist[0])
    temp_bin_flatten = []
    past_bin = temp_hist[1][0]
    for _bin in temp_hist[1][1:]:
        temp_bin_flatten.append((_bin + past_bin) / 2)
        past_bin = _bin
    return temp_hist_probs, temp_bin_flatten
