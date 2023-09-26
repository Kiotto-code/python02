from load_csv import load
import pandas as pd
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
        data = pd.read_csv("population_total.csv")
        print(data)
        if data is None:
            return
        table = load("population_total.csv")
        country1 = "Malaysia"
        country2 = "Japan"
        print(table)
        data = table.transpose()
        print(data)
        # print(data[country1])
        years = np.array(data.index.astype(int))
        country1_data = data[country1].values

        print(data[country1], "\n")
        print(data[country1].values)

        country1_data = [getvalue(i) for i in country1_data]
        country2_data = data[country2].values
        country2_data = [getvalue(i) for i in country2_data]

        plt.plot(years, country1_data, color="green", label=country1)
        plt.plot(years, country2_data, color="blue", label=country2)
        plt.xlabel("Year")
        plt.ylabel("Population")
        # ax.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
        # plt.yticks(np.arange(20000000, y_shape, 20000000))
        plt.gca().yaxis.set_major_formatter(FuncFormatter
                                            (format_tick_with_units))
        # plt.yticks(range(20000000, 80000000, 20000000), \
        #   ["20M", "40M", "60M"])
        # plt.xticks(np.arange(0, 301, 40))
        plt.xticks(range(1800, 2081, 40))
        plt.title("Population Projects")
        plt.legend(loc="lower right")
        plt.show()
    except Exception as e:
        print("Exception Error", e)
    except KeyboardInterrupt:
        print("\rInterrupted signal")


if __name__ == "__main__":
    main()
