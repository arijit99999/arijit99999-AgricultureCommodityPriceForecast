from flask import Flask, request, render_template
import pandas as pd
from prophet import Prophet
import os
import io
import base64
import matplotlib.pyplot as pl
from src.AgricultureCommodityPriceForecast.utlis.utils import load_object

app = Flask(__name__,template_folder='template')

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/forecast', methods=['POST'])
def forecast():
        file = request.files['file']
        
        df = pd.read_csv(file)
        
        if 'commodity' not in df.columns or 'ds' not in df.columns or 'y' not in df.columns:
            return 'Error: DataFrame must contain columns "commodity", "ds", and "y"'
        else:
            n=pd.unique(df['commodity'])
            for x in n:
             df = df[df['commodity'] ==x]
             df.drop('commodity',axis=1,inplace=True)
             model = Prophet()
             model.fit(df)
             future = model.make_future_dataframe(periods=365,freq='D')##we have used day wise
             forecast = model.predict(future)
             fig1 = model.plot(forecast)
             pl.title(f'Forecast with Prophet of {x}')
             pl.xlabel('Date')
             pl.ylabel('Value')
     
             fig2 = model.plot_components(forecast)
           
             img1= io.BytesIO()
             fig1.savefig(img1, format='png')
             img1.seek(0)
             plot_url1= base64.b64encode(img1.getvalue()).decode()
             img2= io.BytesIO()
             fig2.savefig(img2, format='png')
             img2.seek(0)
             plot_url2= base64.b64encode(img2.getvalue()).decode()
             forecast_html= forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].head(30).to_html(index=False)
             forecast_html2= forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail(30).to_html(index=False)
             return render_template('result.html',forecast_html2=forecast_html2,forecast_html=forecast_html,plot_url1=plot_url1,plot_url2=plot_url2,x=x)
             
if __name__ == '__main__':
    app.run()

