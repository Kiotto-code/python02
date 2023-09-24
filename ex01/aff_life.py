import numpy as np
import matplotlib.pyplot as plt
from load_csv import load


def aff_life(country: str):
    """
    Plots the life expectancy of a given country.
    """

    data = load('life_expectancy_years.csv')
    print(data.shape)
    
    data = data.transpose()
    print(data)

    plt.plot(data[country])
    plt.xlabel('Year')
    plt.ylabel('Life Expectancy')
    plt.xticks(np.arange(0, 301, 40))
    plt.title(f'{country} Life Expectancy Projections')

    plt.show()


def main():
    aff_life("Malaysia")


if __name__ == "__main__":
    main()
