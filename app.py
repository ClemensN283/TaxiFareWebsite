import streamlit as st
import datetime
import requests
import joblib

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

'''
# TaxiFareModel front
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')
'''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

1. Let's ask for:
- date and time
- pickup longitude
- pickup latitude
- dropoff longitude
- dropoff latitude
- passenger count
'''
'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''

url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown(
        'Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...'
    )
'''

2. Let's build a dictionary containing the parameters for our API...

3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
'''

st.markdown(''' ### Pickup time and date
''')
#date and time
d = st.date_input("Please provide a date & time", datetime.date(2019, 7, 6))
st.write('Pickup date:', d)

t = st.time_input('Set an alarm for', datetime.time(8, 45))
st.write('Pickup time', t)

st.markdown(''' ### Pickup location
''')
#pickup longitude
pickup_longitude = st.number_input('Insert pickup longitude')
st.write('The longitude for the pickup is ', pickup_longitude)

#pickup latitude
pickup_latitude = st.number_input('Insert pickup latitude')
st.write('The latitude for the pickup is ', pickup_latitude)

st.markdown(''' ### Dropoff location
''')
#dropoff longitude
dropoff_longitude = st.number_input('Insert dropoff longitude')
st.write('The longitude for the dropoff is ', dropoff_longitude)

#dropoff latitude
dropoff_latitude = st.number_input('Insert dropoff latitude')
st.write('The latitude for the dropoff is ', dropoff_latitude)

st.markdown(''' ### Number of passengers
''')
#passenger count
passenger_count = st.number_input('Insert number of passenger')
st.write(passenger_count, ' passengers')




st.markdown('''
            ## Predicted Fare Price
''')
params = dict(key = 'anything',
              pickup_datetime= f"{d} {t}",
              pickup_longitude=pickup_longitude,
              pickup_latitude=pickup_latitude,
              dropoff_longitude=dropoff_longitude,
              dropoff_latitude=dropoff_latitude,
              passenger_count=int(passenger_count))


# retrieve the response
response = requests.get(url, params=params)


if response.status_code == 200:
    print("API call success")
else:
    print("API call error")

response.status_code, response.json().get("prediction",
                                          "no prediction"), response.json()
