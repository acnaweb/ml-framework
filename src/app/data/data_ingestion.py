import logging
import pandas as pd
import pandas_profiling
from settings import RAW_DATASET, CREATE_PROFILER, RAW_REPORT_PROFILER
from utils import serialize_dataset, unserialize_dataset


class ValidationError(Exception):
    pass


class DataIngestion:
    """DataIngestion process to generate the training dataset."""

    def __init__(self) -> None:
        self.dataset = None

    def run_task(self):
        """Run the task"""
        logging.info("start run DataIngestion")

        self.load()

        try:
            self.validate_data()           

        except ValidationError as e:
            logging.error("Invalid dataset: {}".format(e))        
        else:
            self.save()
        finally:
            logging.info("finish run DataIngestion")

    def load(self): 
        """Load data"""
        logging.info("loading data")

        self.dataset =  unserialize_dataset("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")

    
    def validate_data(self):
        """Validation rules"""
        logging.info("validating data")

        if self.dataset.shape[0] != 149:
            raise ValidationError("tamanho inválido {}".format(self.dataset.shape[0]))

    def save(self):
        """Save data"""
        logging.info("saving data")

        serialize_dataset(self.dataset, RAW_DATASET)
        
        if CREATE_PROFILER: 
            profile = pandas_profiling.ProfileReport(self.dataset)
            profile.to_file(RAW_REPORT_PROFILER)

