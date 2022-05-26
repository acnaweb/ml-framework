import click
from training_dataset import ETL

@click.command
def main():
    etl = ETL()
    etl.run_task()

if __name__ == "__main__":
    main()

