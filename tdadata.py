import requests
from config import client_id

endpoint = r"https://api.tdameritrade.com/v1/marketdata/{}/pricehistory".format('GOOG')

payload = { 'apikey':client_id,
			'periodType': 'day',
			'frequencyType':'minute',
			'frequency':'1',
			'period':'2',
			'endDate':'1556158524000',
			'startDate': '1554535854000',
			'needExtendedHoursData':'true'}

content = requests.get(url = endpoint , params = payload)

data = content.json()

print(data)