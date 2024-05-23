
import pandas as pd
import numpy as np
import os
import sys
import matplotlib.pyplot as pl
from src.AgricultureCommodityPriceForecast.logger import logging
from src.AgricultureCommodityPriceForecast.exception import customexception
from prophet import Prophet
import pickle   
class ModelTrainer:
    def __init__(self):
        self.file_path = os.path.join('artifacts','model.pkl')
    def initate_model_training(self,model_data):
        try:
            data=pd.read_csv(model_data)
            logging.info('read model data')
            x=str(input('enter commodity name:  '))
            data=data[data['commodity']==x]
            data.drop('commodity',axis=1,inplace=True)
            model=Prophet()
            logging.info('model saved')
            model.fit(data)
            logging.info('training has been  done')
            y=int(input('enter no of days:  '))
            future = model.make_future_dataframe(periods=y,freq='D')##we have used day wise
            forecast = model.predict(future)
            print(forecast.head())
            fig1 = model.plot(forecast)
            pl.title('Forecast with Prophet')
            pl.xlabel('Date')
            pl.ylabel('Value')
            pl.show()
            fig2 = model.plot_components(forecast)
            pl.show()
        except Exception as e:
            logging.info('Exception occured at Model Training')
            raise customexception(e,sys)