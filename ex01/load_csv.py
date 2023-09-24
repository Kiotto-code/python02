import pandas as pd


def load(path: str):
    """
    Loads a csv file from a given path.
    """
    try:
        data = pd.read_csv(path, index_col=0)
        # data = pd.read_csv(path)
        # data.set_index('country', inplace=True)
        print(f"Loading dataset of dimensions {data.shape}")
        return data
    except Exception as err:
        print(err)
        return None
