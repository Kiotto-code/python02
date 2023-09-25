from load_csv import load 
import matplotlib.ticker as ticker
import matplotlib.pyplot as plt
import numpy as np


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


def main():
    """main function"""
    try:
        data = load("population_total.csv")
        if data is None:
            return
        country1 = "Malaysia"
        country2 = "Belgium"
        data = data.transpose()
        # print(data.shape)
        # print(data)
        years = np.array(data.index.astype(int))
        # print(years)
        country1_data = data[country1].values
        country1_data = [getvalue(i) for i in country1_data]
        country2_data = data[country2].values
        country2_data = [getvalue(i) for i in country2_data]

        plt.plot(years, country1_data, color="green", label=country1)
        plt.plot(years, country2_data, color="blue", label=country2)
        # plt.plot(years, country1_data, color="green", label=country1, scalex=True, scaley=True)
        # plt.plot(years, country2_data, color="blue", label=country2, scalex=True, scaley=True)
        plt.xlabel("Year")
        plt.ylabel("Population")
        # plt.yticks(np.arange(0, 197, 20000000))
        # plt.yticks(range(20, 80, 20))
        # plt.yticks(range(20000000, 80000000, 20000000))
        # plt.yticks([20000000, 40000000, 60000000], ["20M", "40M", "60M"])
        plt.yticks(range(0, 80000000, 20000000), ["0", "20M", "40M", "60M"])
        # plt.yticks(range(20000000, 100000000, 20000000))
        # plt.ylabel('Value (M)')

        # def millions_formatter(x, pos):
        #     return f'{x / 1000000:.0f}'

        # plt.gca().yaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}M'))
        # plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(millions_formatter))
        

        plt.xticks(range(1800, 2081, 40))
        plt.title("Population Projects")
        plt.legend(loc="lower right")
        plt.show()
    except Exception as e:
        print("Exception Error", e)
    except KeyboardInterrupt:
        print("\rInterrupted by user.")


if __name__ == "__main__":
    main()
