import json
import requests

# Simple get request
#response = requests.get( 'https://26607.wayscript.io/' )
#print(response.text)

# get request using a token
calendly_api_key = 'HBFMJLNOFRRIMSDJCOXDXSH4SOVKLBN2'
headers = {
    "X-TOKEN"   :   calendly_api_key
}
response = requests.get( 'https://calendly.com/api/v1/users/me/event_types',
                        headers=headers)

print(response.json())

print( response.json().get('data')[0].get( 'id' ))



# Get requests using a python library
#from alpha_vantage.timeseries import TimeSeries
#ts = TimeSeries(key='RNZPXZ6Q9FEFMEHM',output_format='pandas')
#data, meta_data = ts.get_intraday(symbol='MSFT',interval='1min', outputsize='full')
#print(data)



# Get request to pull data, convert to JSON.
# data_to_use = requests.get('https://26607.wayscript.io/time-series-data')
# data_to_use = data_to_use.json()

'''
# Post Request to use Machine Learning
headers = { 'X-Time-Door-Key'   : 'bf60f73d-fe59-4ccd-ba42-ecb5766ca1dc',
            'Accept'            : 'application/json',
            'Content-Type'      : 'application/json' }

url_base = 'https://api.timedoor.io'

r = requests.post(  url_base + '/invocation/auto-arima',
                    data = open('sample_data.json', 'rb'),
                    headers = headers)

print(r.text)
'''
