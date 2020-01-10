import requests
from config import client_id

def Hist_Data(months):
	endpoint = r"https://api.tdameritrade.com/v1/marketdata/{}/pricehistory".format('$SPX.X')

	payload = { 'apikey':client_id,
				'periodType': 'month',
				'period': str(months),
				'frequencyType':'daily',
				'frequency':'1',
				}

	content = requests.get(url = endpoint , params = payload)
	
	data = content.json()

	data = data['candles']
		
	close =[]
	for i in data:
		close.append(i['close'])
	return close

def Mkt_Direction_Today():
	endpoint = r"https://api.tdameritrade.com/v1/marketdata/{}/quotes".format('$SPX.X')

	payload = {'apikey':client_id,}

	content = requests.get(url = endpoint , params = payload)
	
	data = content.json()

	data= data['$SPX.X']

	return data['netPercentChangeInDouble']

if __name__ == '__main__':
	hist_Data(3)
	Mkt_Direction_Today()
	
	