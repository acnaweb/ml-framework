import pandas as pd
from utils import unserialize_dataset, serialize_dataset
from settings import PROCESSED_DATASET
from model import load, predict

def get_dataset():
    dataset = unserialize_dataset(PROCESSED_DATASET)
    dataset = dataset.drop(["target"], axis=1)
    return dataset   
    
def main():
    logged_model = 'runs:/13edcaa1670540948b350d0e1702efef/model'

    # Load model as a PyFuncModel.
    model = load(logged_model)

    # Predict on a Pandas DataFrame.
    dataset = get_dataset()

    dataset["predicted"] = pd.DataFrame(predict(model,dataset)) 

    serialize_dataset(dataset, "data/processed/predictions.csv")

if __name__ == "__main__":
    main()

