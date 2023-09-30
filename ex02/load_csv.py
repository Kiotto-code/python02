import pandas as pd


def load(path: str):
    """
    Loads a csv file from a given path.
    """
    try:
        # data = pd.read_csv(path)
        # data = pd.read_csv(path)
        data = pd.read_csv(path, index_col=0)
        print(f"Loading dataset of dimensions {data.shape}")
        return data
    except Exception as err:
        print("Exception error: ", err)
        return None
# def load(path: str):
#     """
#     Loads a csv file from a given path.
#     """
#     try:
#         data = pd.read_csv(path, index_col=0)
#         print(f"Loading dataset of dimensions {data.shape}")
#         return data
#     except Exception as err:
#         print("Exception error: ", err)
#         return None
