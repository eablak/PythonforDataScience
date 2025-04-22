from load_csv import load
import matplotlib.pyplot as plt


def display(life_expectancy, income):
    """
    Plots a scatter plot showing the relationship between life expectancy
    and income (GDP per capita) in the year 1900 for different countries.

    Args:
    life_expectancy (pd.DataFrame): DataFrame containing life expectancy data.
    income (pd.DataFrame): DataFrame containing income (GDP per capita) data.
    """
    life_expectancy.set_index("country", inplace=True)
    income.set_index("country", inplace=True)

    life_expectancy = life_expectancy.loc[:, "1900"]
    income = income.loc[:, "1900"]

    plt.scatter(x=income, y=life_expectancy)
    plt.title("1900")
    plt.xlabel("Gross domestic product")
    plt.ylabel("Life Expectancy")
    plt.xscale("log")
    plt.xticks(ticks=[300, 1000, 10000], labels=['300', '1k', '10k'])
    plt.show()


def main():
    """
    Loads the life expectancy and income datasets,then displays a
    scatter plot of life expectancy versus income for the year 1900.
    """
    life_expectancy = load("life_expectancy_years.csv")
    income = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    display(life_expectancy, income)


if __name__ == "__main__":
    main()
