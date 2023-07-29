import os
from mlProject.utils import logger
from mlProject.entity.config_entity import DataTransformationConfig
import pandas as pd
from sklearn.model_selection import train_test_split


class DataTransformation:
    def __init__(self,config: DataTransformationConfig):
        self.config =  config

    def train_test_spliting(self):
        data = pd.read_csv(self.config.data_path)

        train, test = train_test_split(data)

        train.to_csv(os.path.join(self.config.root_dir,'train.csv'),index=False)
        test.to_csv(os.path.join(self.config.root_dir,'test.csv'),index=False)

        logger.info(f"Splited Data into training and test sets")
        logger.info(f"Train Shape => {train.shape}")
        logger.info(f"Test Shape => {test.shape}")

        print(train.shape)
        print(test.shape)
        

    