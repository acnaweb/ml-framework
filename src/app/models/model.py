import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from settings import params


class InvalidModelError(Exception):
    pass


class Model(LogisticRegression): 
     
    def train(self, dataset):
        """Train and test the model instance, from the given dataset."""
        logging.info("start training")

        dataset = dataset[1:]

        X = dataset.drop(["target"], axis=1)
        y = dataset["target"]

        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y, **params)

        self.fit(self.X_train, self.y_train)        

        logging.info("end training ")

        return self

    def validate_training(self):
        """Validate that the training was successful."""
        logging.info("validating training")

        if self.predict([self.X_test.iloc[10]]) != ['Iris-setosa']:
            raise InvalidModelError("Invalid prediction")
        
        