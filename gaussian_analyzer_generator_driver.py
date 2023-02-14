from generate_data import generate_data_driver
from analyze_data import plot_hypothesis


def driver():
    generate_data_driver()
    plot_hypothesis()


if __name__ == '__main__':
    driver()
