import os 
import sys
from src.logger import logging
from src.exception import CustomException

import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.data_transformation import DataTransformation
from src.data_transformation import DataTransformationConfig
from src.components.model_trainer import ModelTrainerConfig, ModelTrainer



@dataclass
class DataIngestionConfig:
    train_data_path: str=os.path.join('artifacts', 'train.csv') #artifacts is a folder, we need to create it, we will create it inside inititate_data_config method.
    test_data_path: str=os.path.join('artifacts', 'test.csv')
    raw_data_path: str=os.path.join('artifacts', 'data.csv')


# inititate above dataingestionconfig class
class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

# To read the data from notebook
    def initiate_data_ingestion(self):
        logging.info("Entered data ingestion method or components")

        try:
            df = pd.read_csv('/home/jagannath/ML_Project/notebook/data/student_details.csv') #here we are reading data from existing directory notebook, we can read data from database as well.
            logging.info('Read the dataset as the dataframe')

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

            logging.info('Train test split initiate')
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)


            df.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            df.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info('Ingestion is completed')

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )



        except Exception as e:
            raise CustomException(e, sys)
        
if __name__=="__main__":
    obj=DataIngestion()
    train_data,test_data=obj.initiate_data_ingestion()

    data_transformation=DataTransformation()
    train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data,test_data)

    
    model_trainer = ModelTrainer()
    print(model_trainer.initiate_model_trainer(train_arr, test_arr))


