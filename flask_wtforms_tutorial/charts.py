'''
This web service extends the Alphavantage api by creating a visualization module, 
converting json query results retuned from the api into charts and other graphics. 

This is where you should add your code to function query the api
'''
import requests
from datetime import datetime
from datetime import date
import pygal


#Helper function for converting date
def convert_date(str_date):
    return datetime.strptime(str_date, '%Y-%m-%d').date()

url = 'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol=IBM&apikey=demo'
r = requests.get(url)
data = r.json()

print(data)

def chooseTimeSeries(TIME_SERIES_WEEKLY):
   url = 'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol=IBM&apikey=demo'
   r = requests.get(url)
   data = r.json(IME_SERIES_WEEKLY)
   return data


def chartType(period):
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo'
    r = requests.get(url)
    data = r.json(interval)
    return data

def getDate(date,convertdate, file):
    getDatesBetween = list()
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo'
    r = requests.get(url)
    data = r.json(interval)
    for num in data:
        getDatesBetween.append()