PHSX815_Project1

The project is composed of two parts.
1. Generating random variables (under two hypotheses) from Gaussian distribution and analyzing them to get 
false negative rate (for fixed standard deviation) and generate plot for LLR distributions
2. From a range of standard deviations, calculate minimum number of measurements needed to 
get false negative rate below a fixed threshold for each standard deviation and plot dependency of 
number of measurements to standard deviation.


<b>Structure and Contents</b>

1. `./outputs/`: Contains all the output files generated - plots, random number dumps, data for generating plots
2. `generate_data.py`: Contains all definitions such as mean of null hypothesis, 
mean of test hypothesis, standard deviation, number of experiments, number of measurements (per experiment), 
sigma range (for second part), alpha, beta. These definitions are then exported everywhere else in the code so modify definitions 
in this file to modify any of these parameters. Draws Gaussian random samples (using numpy) and dumps it into `./outputs/rawdraw_0.txt` (for null hypothesis)
and `./outputs/rawdraw_1.txt` (for test hypothesis). Provides a `generate_data_driver()` to execute all of this logic - used in driver (`gaussian_analyzer_generator_driver.py`).
3. `analyze_data.py`: Reads random values drawn under each hypothesis from `./outputs/rawdraw_0.txt` and `./outputs/rawdraw_1.txt` and 
calculates log likelihood ratio L(X|test hypothesis) / L(X | null hypothesis) for each experiment. Generates a histogram for the log likelihood ratio
and calculates the false negative rate (which is printed to the terminal). The histogram is stored in `./outputs/analyzed_data.png`. Provides a `plot_hypothesis()`
function as to execute all of this logic - used in driver (`gaussian_analyzer_generator_driver.py`).
4. `gaussian_analyzer_generator_driver.py`: A driver wrapper for two functions: `generate_data_driver()` and `plot_hypothesis()`. `generate_data_driver()` generates and dumps the random variables drawn to a file. `plot_hypothesis()` is the driver to load random variables and then analyze them (generate LLR histograms - see above) . Just a simple wrapper for drivers from `generate_data.py` and `analyze_data.py`.
5. `get_min_n_fnr.py`: Takes in range of standard deviation and for each standard deviation, calculates the minimum number 
of measurements needed to get false negative ratio below a threshold (the threshold beta is imported from `generate_data.py`). 
Dumps list of pairs of number of measurements and standard deviations into `./outputs/n_sigma_variation.txt`. Provides a `write_min_n_variation_driver()` function 
to execute all this logic - used in driver (`min_n_variation_driver.py`)
6. `analyze_min_n_fnr.py`: Loads pair of number of measurements and standard deviations from `./outputs/n_sigma_variation.txt` 
and generates plot of number of measurements vs standard deviation. Saves the plot in `./outputs/n_sigma_variation.png`. Provides a `n_std_variation_plot_driver()`
function to execute all this logic - used in driver (`min_n_variation_driver.py`)
7. `min_n_variation_driver.py`: A driver wrapper for two functions: `write_min_n_variation_driver()` and `n_std_variation_plot_driver()`. `write_min_n_variation_driver()` calculates 
and stores number of measurements and corresponding standard deviations to a file. `n_std_variation_plot_driver()` loads that file and generates a plot. See Above.
8. `file_list_utils.py`: Contains functions to load and write lists to and from txt files simpler. Also supports multidimensional lists.
9. `histogram_utils.py`: File contains `get_histogram_data()` which takes in measurements and number of samples and first generates a histogram using numpy (but doesn't plot it) and then returns a 2-d list of bins and probability at each bin which is used to plot. I had to implement this since MatPlotLib's histogram was slow for 1,000,000+ experiments.
10. `perf_wrapper.py`: A basic wrapper to measure performance of functions. Not currently used anywhere.

<b>Part 1: Generating random variables (under two hypotheses) from Gaussian distribution and analyzing them to get 
false negative rate (for fixed standard deviation) and generate plot for LLR distributions</b><br/><br/>
To run the code for this part, type `python3 gaussian_analyzer_generator_driver.py`. <br/><br/>
`gaussian_analyzer_generator_driver.py` has a two functions. 
<br/><br/>a. `generate_data_driver()` draws n_experiments samples from normal distribution with defined means and standard deviation and exports raw data to `rawdraw_0.txt` (null hypothesis) and `rawdraw_1.txt` (test hypothesis). These export files are located in `./outputs` directory
<br/><br/>b. `plot_hypothesis()` analyzes the raw data generated, calculates the LLR distributions and also calculates false negative rate. The plot generated by this driver is stored in `./outputs/analyzed_data.png`.

<b>Part 2: From a range of standard deviations, calculate minimum number of measurements needed to 
get false negative rate below a fixed threshold for each standard deviation and plot dependency of 
number of measurements to standard deviation.</b><br/><br/>
To run the code for this part, type `python3 min_n_variation_driver.py`. <br/><br/>
`min_n_variation_driver.py` also has two functions
<br/><br/>a. `write_min_n_variation_driver()` calculates the minimum number of measurements for a range of standard deviations which get the false negative rate below a threshold. The function lacks in performance (since it has to draw a lot of samples for each number of measurement iteration) so I'll recommend decreasing `N_experiments` in `generate_data.py`. Each pair of number of measurements and standard deviation is written to `./outputs/n_sigma_variation.txt`.
<br/><br/>b. `n_std_variation_plot_driver()` loads the number of measurements and standard deviation pair from `./outputs/n_sigma_variation.txt` and plots them in a graph which is saved in `./outputs/n_sigma_variation.png`.
