import streamlit as st
from datetime import *
import requests
import pandas as pd
import numpy as np

st.markdown(
'''
# Predict your Taxi for your next ride
'''
)

pickup_datetime = datetime.now()
pickup_longitude = 0
pickup_latitude = 0
dropoff_longitude = 0
dropoff_latitude = 0

st.markdown(''' ### Pickup time and date''')
#date and time
pickup_datetime = st.text_input('Please enter time & date', value=pickup_datetime)

st.markdown(''' ### Pickup & dropoff location''')
#pickup longitude
pickup_longitude = st.text_input('Insert pickup longitude', value=pickup_longitude)
#pickup latitude
pickup_latitude = st.text_input('Insert pickup latitude', value=pickup_latitude)
#dropoff longitude
dropoff_longitude = st.text_input('Insert dropoff longitude', value=dropoff_longitude)
#dropoff latitude
dropoff_latitude = st.text_input('Insert dropoff latitude', value=dropoff_latitude)

st.markdown(''' ### Number of passengers''')
#passenger count
passenger_count = int(st.selectbox('Select number of passenger', [1,2,3,4,5,6,7,8,9]))



st.markdown('''
            ## Predicted Fare Price ''')

params = dict(key = 'anything',
                pickup_datetime=pickup_datetime,
                pickup_longitude=pickup_longitude,
                pickup_latitude=pickup_latitude,
                dropoff_longitude=dropoff_longitude,
                dropoff_latitude=dropoff_latitude,
                passenger_count=int(passenger_count))

url = 'https://taxifare.lewagon.ai/predict'
# retrieve the response
response = requests.get(url, params=params)


if response.status_code == 200:
    print("API call success")
else:
    print("API call error")

response.status_code
predicted_price = response.json().get("prediction",
                                            "no prediction")
st.markdown(f'# {predicted_price}')

@st.cache
def get_map_data():


    return pd.DataFrame(
        dict(lat=[float(pickup_latitude),
                  float(dropoff_latitude)],
             lon=[float(pickup_longitude),
                  float(dropoff_longitude)]))


df = get_map_data()

st.map(df)
