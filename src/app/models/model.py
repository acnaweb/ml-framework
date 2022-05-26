import logging
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
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

        print(self.score(self.X_test_transform, self.y_test))

        y_predictions = self.predict(self.X_test_transform)    

        if y_predictions[0] != "Iris-virginica":
            raise InvalidModelError("Invalid prediction {}".format(y_predictions[0]))
        
    def serialize(self):
        """Serialize current model instance into a stream of bytes."""
        return pickle.dumps(self)