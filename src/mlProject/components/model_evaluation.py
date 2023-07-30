import os
import pandas as pd
from sklearn.metrics import mean_absolute_error,mean_squared_error, r2_score
from urllib.parse import urlparse
import mlflow
import mlflow.sklearn
import numpy as np
import joblib
from pathlib import Path
from mlProject.entity.config_entity import ModelEvaluationConfig
from mlProject.utils.comman import save_json


class ModelEvaluation:
    def __init__(self,config: ModelEvaluationConfig):
        self.config = config

    def eval_metrics(self,actual, pred):
        rmse = np.sqrt(mean_squared_error(actual,pred))
        mae = mean_absolute_error(actual,pred)
        r2 = r2_score(actual,pred)
        return {"rmse":rmse,"mae":mae,"r2":r2}
    
    def log_into_mlfow(self):

        test_data = pd.read_csv(self.config.test_data)
        model = joblib.load(self.config.model_path)

        test_x =  test_data.drop([self.config.target_column],axis=1)
        test_y = test_data[[self.config.target_column]]

        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_url_type_store =  urlparse(mlflow.get_tracking_uri()).scheme
        print(tracking_url_type_store,mlflow.get_tracking_uri(),urlparse(mlflow.get_tracking_uri()))

        with mlflow.start_run():
            predictions = model.predict(test_x)

            scores =  self.eval_metrics(test_y,predictions)

            save_json(path=Path(self.config.metric_file_name),data=scores)

            mlflow.log_params(self.config.all_params)
            mlflow.log_metrics(scores)

            if tracking_url_type_store != 'file':
                mlflow.sklearn.log_model(model,"model",registered_model_name='ElasticModel')
            else:
                mlflow.sklearn.log_model(model,'model')

