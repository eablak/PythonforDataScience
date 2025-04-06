from load_csv import load
import matplotlib.pyplot as plt


def display(life_expectancy, income):

    life_expectancy.set_index("country", inplace=True)
    income.set_index("country", inplace=True)

    life_expectancy = life_expectancy.loc[:, "1900"]
    income = income.loc[:, "1900"]

    plt.scatter(x=income, y=life_expectancy)
    plt.title("1900")
    plt.xlabel("Life Expectancy")
    plt.ylabel("Gross domestic product")
    plt.xscale("log")
    plt.xticks(ticks=[300, 1000, 10000], labels=['300', '1k', '10k'])
    plt.show()


def main():

    life_expectancy = load("life_expectancy_years.csv")
    income = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    display(life_expectancy, income)


if __name__ == "__main__":
    main()
