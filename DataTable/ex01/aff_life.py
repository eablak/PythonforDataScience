from load_csv import load
import matplotlib.pyplot as plt


def main():
    """
    This script loads life expectancy data from a CSV file and visualizes
    Turkey's life expectancy over the years using a line plot.
    """
    try:
        df = load("life_expectancy_years.csv")
        df.set_index("country", inplace=True)
        x = df.loc["Turkey"]
        x.plot()
        plt.title("Turkey Life expectancy Projections")
        plt.xlabel("Year")
        plt.ylabel("Life expectancy")
        plt.yticks([30, 40, 50, 60, 70, 80, 90],
                   ["30", "40", "50", "60", "70", "80", "90"])
        plt.show()
    except Exception as msg:
        print(f"Unexpected error! {msg}")


if __name__ == "__main__":
    main()
