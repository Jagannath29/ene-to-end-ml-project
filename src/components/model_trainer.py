# Libraries

import os
import sys
from dataclasses import dataclass


from catboost import CatBoostRegressor
from sklearn.ensemble import (
    AdaBoostRegressor,
    GradientBoostingRegressor,
    RandomForestRegressor
)
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor
from xgboost import XGBRegressor

from src.exception import CustomException
from src.logger import logging

from src.utils import save_object,  evaluate_models


@dataclass
class ModelTrainerConfig:
    trainer_model_file_path = os.path.join('artifacts', 'model.pkl')

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()


    def initiate_model_trainer(self, train_array, test_array):
        try:
            logging.info('Splitting training and testing')
            xtrain,ytrain,xtest,ytest=(
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1]
            )


            models = {
                'Random Forest': RandomForestRegressor(),
                'Decision Tree': DecisionTreeRegressor(),
                'Gradient Boosting': GradientBoostingRegressor(),
                'Linear Regressor': LinearRegression(),
                'k-neighbours ': KNeighborsRegressor(),
                'Xg Regressor': XGBRegressor(),
                'Catboost Regressor': CatBoostRegressor(),
                'AdaBoost Regressor': AdaBoostRegressor(),

            }

            
            model_report:dict=evaluate_models(X_train=xtrain,y_train=ytrain,X_test=xtest,y_test=ytest,
                                             models=models)
            
            ## To get best model score from dict
            best_model_score = max(sorted(model_report.values()))

            ## To get best model name from dict

            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]
            best_model = models[best_model_name]

            if best_model_score<0.6:
                raise CustomException("No best model found")
            logging.info(f"Best found model on both training and testing dataset")

            save_object(
                file_path=self.model_trainer_config.trainer_model_file_path,
                obj=best_model
            )

            predicted=best_model.predict(xtest)

            r2_square = r2_score(ytest, predicted)
            return r2_square


        except Exception as e:
            raise CustomException(e, sys)