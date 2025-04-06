from load_csv import load
import matplotlib.pyplot as plt


def display(df):

    df.set_index("country", inplace=True)
    x = df.loc["Turkey"]
    x.plot()
    plt.title("Turkey Life expectancy Projections")
    plt.xlabel("Year")
    plt.ylabel("Life expectancy")
    plt.yticks([30, 40, 50, 60, 70, 80, 90],
               ["30", "40", "50", "60", "70", "80", "90"])
    plt.show()


def main():
    df = load("life_expectancy_years.csv")
    display(df)


if __name__ == "__main__":
    main()
