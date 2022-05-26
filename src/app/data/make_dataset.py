import logging
from data_ingestion import DataIngestion
from data_prep import DataPreparation
from settings import *

def main():
    logging.info("*** start making dataset ***")
    
    # perform data ingestion
    dataIngestion = DataIngestion()
    dataIngestion.run_task()

    # performe data preparation
    dataPreparation = DataPreparation()
    dataPreparation.run_task()

    logging.info("*** finish making dataset ***")

if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)

    print_settings()
    main()

