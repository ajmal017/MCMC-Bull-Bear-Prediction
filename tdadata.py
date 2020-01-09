import requests
from config import client_id

if __name__ == '__main__':
	endpoint = r"https://api.tdameritrade.com/v1/marketdata/{}/pricehistory".format('DG')

	payload = { 'apikey':client_id,
				'periodType': 'day',
				'period': '2',
				'frequencyType':'minute',
				'frequency':'1',
				'period':'2'
				}

	content = requests.get(url = endpoint , params = payload)
	

	data = content.json()
	
	print(data)