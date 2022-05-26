import logging
import pandas as pd

logging.basicConfig(format='%(asctime)s %(message)s', level=logging.DEBUG)


class ValidationError(Exception):
    pass

class ETL:
    """Encapsulate ETL process to generate the training dataset."""

    def run_task(self):
        """Run the task"""
        logging.info("start run ETL")

        dataset = self.generate_data();

        try:
            self.validate_data(dataset)
        except ValidationError as e:
            logging.error("Invalid dataset: {}".format(e))
        else:
            self.save(dataset)
        finally:
            logging.info("finish run ETL")

    def generate_data(self): 
        """Extraction and transformation"""
        logging.info("generating data")

        df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data", sep=",")

        return df;
    
    def validate_data(self, dataset):
        """Validation rules"""
        logging.info("validating data")

        if dataset.shape[0] != 149:
            raise ValidationError("tamanho inválido {}".format(dataset.shape[0]))

    def save(self, dataset:pd.DataFrame):
        """Save data"""
        logging.info("saving data")

        dataset.to_csv("src/app/data/raw/dataset.csv")
        