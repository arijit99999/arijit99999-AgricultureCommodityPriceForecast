from src.AgricultureCommodityPriceForecast.components.data_ingestion import data_ingestion
from  src.AgricultureCommodityPriceForecast.components.data_transformation import data_transformation
from src.AgricultureCommodityPriceForecast.components.model_trainer import ModelTrainer


import os
import sys
from src.AgricultureCommodityPriceForecast.logger import logging
from src.AgricultureCommodityPriceForecast.exception import customexception


obj1=data_ingestion()
raw_data_path=obj1.initiate_data_ingestion()

obj2=data_transformation()
model_data_path=obj2.data_transform_initiated(raw_data_path)


obj3=ModelTrainer()
model_path=obj3.initate_model_training(model_data_path)
