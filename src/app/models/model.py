import logging
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score

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

        self.scaler = StandardScaler()
        self.X_train_transform = self.scaler.fit_transform(self.X_train)
        self.X_test_transform = self.scaler.transform(self.X_test)

        self.fit(self.X_train_transform, self.y_train)                  

        logging.info("end training ")

        return self


    def validate_training(self):
        """Validate that the training was successful."""
        logging.info("validating training")
       

    def serialize(self):
        """Serialize current model instance into a stream of bytes"""
        return pickle.dumps(self)


    def evaluate_performance(self, y_test, y_pred):
        accuracy = accuracy_score(y_test, y_pred)
        f1_macro = f1_score(y_test, y_pred, average='macro')
        f1_micro = f1_score(y_test, y_pred, average='micro')
        precision = precision_score(y_test, y_pred, average='micro')
        recall = recall_score(y_test, y_pred, average='micro')
   
        return accuracy, precision, recall, f1_micro, f1_macro
