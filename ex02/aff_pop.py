import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from load_csv import load


def convert_to_numeric(value_str):
    # Define a dictionary to map prefix multipliers to their values
    multipliers = {'k': 1e3, 'm': 1e6}

    # Extract the numeric part of the string
    numeric_part = float(value_str.rstrip('kmKM'))

    # Get the last character to determine the multiplier
    multiplier = value_str[-1].lower()

    # Multiply the numeric part by the multiplier's value
    return numeric_part * multipliers.get(multiplier, 1)

def aff_pop(country: str):
    """
    Plots the population of a given country.
    """
    data = load('population_total.csv')
    data = data.transpose()
    df = pd.DataFrame(data)
    print(df)
    input()

    # Apply the conversion function to the DataFrame column
    df[country] = df[country].apply(convert_to_numeric)

    # Print the updated DataFrame
    print(df)

    # plt.plot(data[country])
    plt.plot(data[country])
    print(data)
    plt.xlabel('Year')
    plt.ylabel('Population')
    plt.xticks(np.arange(0, 301, 40))
    plt.title(f'{country} Population Projections')
    plt.show()


aff_pop("Malaysia")
