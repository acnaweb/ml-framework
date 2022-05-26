import logging
import click
from data_ingestion import DataIngestion
from data_prep import DataPreparation

@click.command
def main():
    
    # perform data ingestion
    dataIngestion = DataIngestion()
    dataIngestion.run_task()

    # performe data preparation
    dataPreparation = DataPreparation()
    dataPreparation.run_task()


if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s %(message)s', level=logging.WARN)

    main()
