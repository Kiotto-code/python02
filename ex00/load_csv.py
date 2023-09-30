import pandas as pd


def load(path: str) -> pd.core.frame.DataFrame:
    """
    Loads a csv file from a given path.
    """
    try:
        data = pd.read_csv(path, index_col=0)
        # print(data.head(1).index[0])
        # data['country'] = data.loc[:, 'country'].str.strip()
        print(f"Loading dataset of dimensions {data.shape}")
        return data
    except Exception as e:
        print(e)
        return None
