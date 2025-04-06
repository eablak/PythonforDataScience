from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt


def display(df):

    df.set_index("country", inplace=True)
    df = pd.concat([df.loc["Turkey", "1800":"2050"],
                    df.loc["France", "1800":"2050"]], axis=1)
    df = df.replace({"M": ""}, regex=True).astype(float)

    x_turkey = df["Turkey"]
    x_france = df["France"]

    x_turkey.plot(label="Turkey")
    x_france.plot(label="France")

    plt.legend()

    plt.title("Population Projections")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.yticks([20, 40, 60], ["20M", "40M", "60M"])
    plt.show()


def main():
    df = load("population_total.csv")
    display(df)


if __name__ == "__main__":
    main()
