"""
General app's level configuration items.
"""

import logging

params = {
    "test_size": 0.33, 
    "random_state": 42
}

PROCESSED_DATASET = "data/processed/dataset.csv"
EXPERIMENT_NAME = "iris-demo"
MLFLOW_REMOTE_URI = "0.0.0.0:5000"


def print_settings():
    logging.info("*** model parameters ***")

    logging.info("params={}".format(params))
   
