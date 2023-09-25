from load_csv import load
import matplotlib.pyplot as plt


def scatter(year: str):
    """
    Load the life expectancy dataset and plot the life expectancy of 1900 \
    against the GDP of 1900.
    """
    try:
        gdp_data = load(
            "income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
        gdp_data = gdp_data.loc[:, year]
        life_data = load("life_expectancy_years.csv")
        life_data = life_data.loc[:, year]

        plt.title(year)
        plt.xlabel("Gross domestic product")
        plt.ylabel("Life Expectancy")
        plt.scatter(gdp_data, life_data)
        plt.xscale("log")
        plt.xticks([300, 1000, 10000], ["300", "1k", "10k"])

        plt.show()
        plt.savefig("1900.jpg")
    except Exception as err:
        print(err)
        return


def main():
    scatter("1900")


if __name__ == "__main__":
    main()
