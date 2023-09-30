from load_csv import load
# import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FuncFormatter


def getvalue(string: str) -> int:
    """get value from string"""
    value = 1
    if string[-1] == "M":
        value = 1000000
    elif string[-1] == "k":
        value = 1000
    else:
        return float(string)
    return float(string[:-1]) * value


def format_tick_with_units(value, pos):
    """Formats a tick with a number and a unit."""
    if abs(value) >= 1e9:
        return f'{value / 1e9:.1f}B'
    elif abs(value) >= 1e6:
        return f'{value / 1e6:.0f}M'
    elif abs(value) >= 1e3:
        return f'{value / 1e3:.0f}K'
    else:
        return str(int(value))


def main():
    """main function to compare population of two countries"""
    try:
        table = load("population_total.csv")
        table = table.loc[:, "1800":"2050"]

        country1 = "Malaysia"
        country2 = "Japan"
        data = table.transpose()

        country1_data = data[country1]
        print(country1_data)
        country1_data = country1_data.apply(getvalue)
        print(country1_data)
        country2_data = data[country2]
        country2_data = country2_data.apply(getvalue)

        plt.plot(country1_data, color="green", label=country1)
        plt.plot(country2_data, color="blue", label=country2)
        plt.xlabel("Year")
        plt.ylabel("Population")
        plt.gca().yaxis.set_major_formatter(FuncFormatter
                                            (format_tick_with_units))
        plt.xticks(np.arange(0, 251, 40))
        plt.title("Population Projects")
        plt.legend(loc="lower right")
        plt.show()
    except Exception as e:
        print("Exception Error", e)
    except KeyboardInterrupt:
        print("\rInterrupted signal")


if __name__ == "__main__":
    main()
