import logging
from model import Model
from experiment import perform_experiment
from settings import *
from utils import unserialize_dataset
from settings import PROCESSED_DATASET, EXPERIMENT_NAME
# mlflow tracking
import mlflow


def do_train():
    logging.info("*** start training model ***")
    
    # training model
    dataset = unserialize_dataset(PROCESSED_DATASET)

    # create experiment id for tracking using mlflow
    experiment = mlflow.get_experiment_by_name(EXPERIMENT_NAME)
    if experiment == None:
        exp_id = mlflow.create_experiment(EXPERIMENT_NAME)
    else:
        exp_id = experiment.experiment_id        

    perform_experiment(Model(), dataset, exp_id)

    logging.info("*** finish training model ***")

if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)

    print_settings()
    do_train()

