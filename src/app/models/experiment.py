# mlflow tracking
import mlflow
import mlflow.sklearn
# others
import time
import logging

def track_performance_metrics(accuracy, precision, recall, f1_micro, f1_macro,
                              accuracy_train, precision_train, recall_train, f1_micro_train, f1_macro_train,
                              training_time, prediction_time):
    # performance test set
    mlflow.log_metric('accuracy', accuracy)
    mlflow.log_metric('f1_macro', f1_macro)
    mlflow.log_metric('f1_micro', f1_micro)
    mlflow.log_metric('precision', precision)
    mlflow.log_metric('recall', recall)

    # performance train set
    mlflow.log_metric('accuracy_train', accuracy_train)
    mlflow.log_metric('f1_macro_train', f1_macro_train)
    mlflow.log_metric('f1_micro_train', f1_micro_train)
    mlflow.log_metric('precision_train', precision_train)
    mlflow.log_metric('recall_train', recall_train)
    
    mlflow.log_metric('training_time', training_time)
    mlflow.log_metric('prediction_time', prediction_time)


def perform_experiment(model, dataset, exp_id):
    logging.info("experiment id {}".format(exp_id))

    with mlflow.start_run(experiment_id = exp_id):
        mlflow.sklearn.autolog()
        
        # training model
        start_training = time.time()
        model.train(dataset)
        end_training = time.time()

        # validate model
        model.validate_training()

        # predict the test set
        start_prediction = time.time()    
        y_pred = model.predict(model.X_test_transform)  
        end_prediction = time.time()

        # evaluate performance test
        accuracy, precision, recall, f1_micro, f1_macro = model.evaluate_performance(model.y_test, y_pred)


        # predict the test train
        start_prediction = time.time()    
        y_pred_train = model.predict(model.X_train_transform)  
        end_prediction = time.time()

        # evaluate performance test
        accuracy_train, precision_train, recall_train, f1_micro_train, f1_macro_train = model.evaluate_performance(model.y_train, y_pred_train)
                 
        training_time = end_training - start_training
        prediction_time = end_prediction - start_prediction
        
        # Track performance metrics
        track_performance_metrics(accuracy, precision, recall, f1_micro, f1_macro,
                              accuracy_train, precision_train, recall_train, f1_micro_train, f1_macro_train,
                              training_time, prediction_time)