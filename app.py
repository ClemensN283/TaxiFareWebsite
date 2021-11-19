import streamlit as st
import datetime
import requests



'''
# TaxiFareModel front
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


col1, col2, col3 = st.columns(3)
col1.metric("Pickup Location", pickup_longitude)
col2.metric("FTEC", "$121.10", "0.46%")
col3.metric("BTC", "$46,583.91", "+4.87%")

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

url = 'https://taxifare.lewagon.ai/predict'
# retrieve the response
response = requests.get(url, params=params)


if response.status_code == 200:
    print("API call success")
else:
    print("API call error")

response.status_code, response.json().get("prediction",
                                            "no prediction"), response.json()
