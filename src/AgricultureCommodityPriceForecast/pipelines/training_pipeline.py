from src.AgricultureCommodityPriceForecast.components.data_ingestion import data_ingestion




import os
import sys
from src.AgricultureCommodityPriceForecast.logger import logging
from src.AgricultureCommodityPriceForecast.exception import customexception


obj1=data_ingestion()
row_data=obj1.initiate_data_ingestion()