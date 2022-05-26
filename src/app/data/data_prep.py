import logging
import pandas as pd
import pandas_profiling
from settings import PROCESSED_DATASET, RAW_DATASET, PROCESSED_REPORT_PROFILER, CREATE_PROFILER


class DataPreparationError(Exception):
    pass


class DataPreparation:
    """Dataset preparation"""
        
    def run_task(self):
        """Run the task"""
        logging.info("start run DataPreparation")

        self.load()
                
        self.set_header()
        self.add_feature()
        self.drop_feature()        
        self.do_imputation()
        self.do_missing_value()
        self.do_resampling()
        self.do_transform()
        
        self.save()

        logging.info("finish DataPreparation")
    

    def load(self): 
        """Load data"""
        logging.info("loading data")

        self.dataset = pd.read_csv(RAW_DATASET, sep=",")
   
    def save(self):
        """Save data"""
        logging.info("saving data")

        self.dataset.to_csv(PROCESSED_DATASET, index=False)

        if CREATE_PROFILER: 
            profile = pandas_profiling.ProfileReport(self.dataset)
            profile.to_file(PROCESSED_REPORT_PROFILER)


    def set_header(self):
        columns = ["sepal length in cm", "sepal width in cm", "petal length in cm", "petal width in cm", "target"]
        self.dataset.columns = columns

    def add_feature(self):        
        pass

    def drop_feature(self):
        pass

    def do_imputation(self):
        pass

    def do_missing_value(self):
        pass

    def do_transform(self):
        pass

    def do_resampling(self):
        pass
