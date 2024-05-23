import pandas as pd
import os
import sys
from src.AgricultureCommodityPriceForecast.logger import logging
from src.AgricultureCommodityPriceForecast.exception import customexception

class dataingestionConfig:
    raw_data=os.path.join("artifacts","raw.csv")


class data_ingestion:
    def __init__(self):
        self.ingestion_config=dataingestionConfig()
        
    
    def initiate_data_ingestion(self):
        logging.info("data ingestion started")
        
        try:
           data=pd.read_csv(r"C:\Users\deyar\OneDrive\Desktop\AgricultureCommodityForecast\notebooks\data\agricultuer.csv") 
           os.makedirs(os.path.dirname(os.path.join(self.ingestion_config.raw_data)),exist_ok=True) 
           data.to_csv(self.ingestion_config.raw_data,index=False) 
           return self.ingestion_config.raw_data
           logging.info('row data saved ') 
        except Exception as e:
           logging.info("exception during occured at data ingestion stage")
           raise customexception(e,sys)