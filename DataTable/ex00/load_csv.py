import pandas as pd


def load(path: str) -> pd.DataFrame:
    """
    Load a CSV file into a pandas DataFrame.

    :param path: Path to the CSV file.
    :return: DataFrame if successful, else None.
    """
    if (isinstance(path, str) is False):
        return None
    try:
        df = pd.read_csv(path)
        print(f"Loading dataset of dimensions {df.shape}")
        return df
    except FileNotFoundError:
        print("Csv file not found!")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None
