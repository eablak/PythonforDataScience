import pandas as pd


def load(path: str) -> pd.DataFrame:

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
        print(f"Unexpecte error: {e}")
        return None
