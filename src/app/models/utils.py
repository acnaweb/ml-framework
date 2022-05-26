import pandas as pd

def serialize_dataset(dataset, filename) -> bytes:
    dataset.to_csv(filename, index=False)

def unserialize_dataset(filename) -> object:
    return pd.read_csv(filename, sep=",")