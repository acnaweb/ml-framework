import logging
import click
from model import Model
from settings import *
from utils import unserialize_dataset
from settings import PROCESSED_DATASET

def do_train():
    logging.info("*** start training model ***")
    
    # training model
    dataset = unserialize_dataset(PROCESSED_DATASET)
    model = Model()
    model.train(dataset)
    model.validate_training()

    logging.info("*** finish training model ***")

if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)

    print_settings()
    do_train()

