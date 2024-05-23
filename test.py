from flask import Flask, request, render_template, redirect, url_for
import pandas as pd
from prophet import Prophet
import io
import base64
import matplotlib.pyplot as plt

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/forecast', methods=['POST'])
def forecast():
        # Get the uploaded file
        file = request.files['file']
        
        # Read the file into a pandas DataFrame
        df = pd.read_csv(file)
        
        # Check the required columns 'commodity', 'ds', and 'y'
        if 'commodity' not in df.columns or 'ds' not in df.columns or 'y' not in df.columns:
            return 'Error: DataFrame must contain columns "commodity", "ds", and "y"'
        
        # Get unique commodities
        commodities = df['commodity'].unique()
        plots = []

        for commodity in commodities:
            # Filter data for the current commodity
            commodity_df = df[df['commodity'] == commodity]
            commodity_df.drop('commodity',axis=1,inplace=True)
            # Initialize the Prophet model and fit it
            model = Prophet()
            model.fit(commodity_df)

            # Create a future dataframe and make predictions
            future = model.make_future_dataframe(periods=30)
            forecast = model.predict(future)

            # Plot the forecast
            fig = model.plot(forecast)
            plt.title(f'Forecast for {commodity}')
            plt.xlabel('Date')
            plt.ylabel('Price')
            
            # Save the plot to a BytesIO object
            img = io.BytesIO()
            fig.savefig(img, format='png')
            img.seek(0)
            plot_url = base64.b64encode(img.getvalue()).decode()
            plots.append((commodity, plot_url))

            plt.close(fig)  # Close the plot to free up memory

        return render_template('result.html', plots=plots)

if __name__ == '__main__':
    app.run(debug=True)

