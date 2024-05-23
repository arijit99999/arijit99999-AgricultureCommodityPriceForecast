import os
import sys
import pandas as pd
from src.AgricultureCommodityPriceForecast.logger import logging
from src.AgricultureCommodityPriceForecast.exception import customexception
import numpy as np



class datatransformationconfig:
    model_path=os.path.join("artifacts","model_data.csv")
class data_transformation:
    def __init__(self):
        self.model_path=datatransformationconfig()
        
    def data_transform_initiated(self,data):
       try:
          logging.info('trasnformation initiated')
          model_data=pd.read_csv(data)
          model_data.drop(['Unnamed: 0'],axis=1,inplace=True)
          model_data.columns=['commodity','ds','y']
          model_data.to_csv(self.model_path.model_path,index=False)
          logging.info('this is our model data')
          return self.model_path.model_path
       except Exception as e:
          logging.info("exception during occured at data tarnsformation initiation stage")
          raise customexception(e,sys)