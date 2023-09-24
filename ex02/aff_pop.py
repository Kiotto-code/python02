import matplotlib.pyplot as plt
import numpy as np
from load_csv import load


def aff_pop(country: str):
    """
    Plots the population of a given country.
    """
    data = load('population_total.csv')
    data = data.transpose()

    # plt.plot(data[country])
    plt.plot(data[country])
    print(data)
    plt.xlabel('Year')
    plt.ylabel('Population')
    plt.xticks(np.arange(0, 301, 40))
    plt.title(f'{country} Population Projections')
    plt.show()


aff_pop("Malaysia")
