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
        finally:
            logging.info("finish run ETL")

    def generate_data(self): 
        """Extraction and transformation"""

        return None;
    
    def validate_data(self, dataset):
        raise ValidationError("tamanho inválido")