import numpy as np
import matplotlib.pyplot as plt
from load_csv import load


def aff_life(country: str):
    """
    Plots the life expectancy of a given country.
    """

    data = load('life_expectancy_years.csv')
    print(data)

    data = data.transpose()
    print(data)

    plt.plot(data[country])
    plt.xlabel('Year')
    plt.ylabel('Life Expectancy')
    print("check data[country].shape", data[country].shape)
    plt.xticks(np.arange(0, 301, 40))
    # plt.xticks(range(1800, 2081, 40))
    plt.title(f'{country} Life Expectancy Projections')

    plt.show()


def main():
    """main"""
    try:
        aff_life("Malaysia")
    except Exception as e:
        print("Exception Error", e)
    except KeyboardInterrupt:
        print("KeyboardInterrupt")


if __name__ == "__main__":
    main()
