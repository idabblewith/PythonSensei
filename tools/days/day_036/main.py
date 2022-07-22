from days.day_036.files.helpers import *

def day_036():
	title("STOCK NOTIFIER")
	with open('./tools/secrets/newsapikey.secret') as newsapifile:
		news_key = newsapifile.read()

	with open('./tools/secrets/stock_api.secret') as stockfile:
		stock_key = stockfile.read()

	with open('./tools/secrets/twilio_id.secret') as asid:
		acc_sid = asid.read()

	with open('./tools/secrets/twilio_num.secret') as twinum:
		twil_num = twinum.read()

	with open('./tools/secrets/twilio_token.secret') as twi:
		twi_token = twi.read()

	with open('./tools/secrets/my_num.secret') as myn:
		my_num = myn.read()


	STOCK = "TSLA"
	COMPANY_NAME = "Tesla"
	FUNCTION = "TIME_SERIES_DAILY"
	今日 = dt.utcnow().date()
	昨日 = 今日 - td(days=1)
	一昨日 = 今日 - td(days=2)

	stock_params = {
		"apikey":stock_key,
		"symbol":STOCK,
		"function":FUNCTION,
		"outputsize":"compact"
	}
	stock_response = requests.get("https://www.alphavantage.co/query", params=stock_params)
	stock_response.raise_for_status()
	データ = stock_response.json()
	日データ = データ["Time Series (Daily)"]
	昨日のデータ = 日データ[str(昨日)]
	一昨日のデータ = 日データ[str(一昨日)]

	news_params = {
		"apiKey":news_key,
		"q":COMPANY_NAME,
		"pageSize":3,
		"country":"us"
	}

	news_response = requests.get("https://newsapi.org/v2/top-headlines", params=news_params)
	news_response.raise_for_status()
	news_data = news_response.json()["articles"]
	if len(news_data) < 3:
		endrange = len(news_data)
	else: endrange = 3

	yesterdays_close = float(昨日のデータ["4. close"])
	day_before_yd_close = float(一昨日のデータ["4. close"])
	difference =  day_before_yd_close - yesterdays_close
	percentage_change = difference/day_before_yd_close * 100

	articles = {}
	for artnum in range(0,endrange): 
		articles[artnum+1] = \
			{
				"Headline":news_data[artnum]["title"],
				"Brief":news_data[artnum]["description"]
			}

	def show_news():
		news = ""
		for num in articles:        
			news+= f'\nHeadline: {articles[num]["Headline"]}\nBrief: {articles[num]["Brief"]}\n'
		return news


	client = Client(acc_sid, twi_token)

	if yesterdays_close > (day_before_yd_close*1.05):
		message  = client.messages.create(
			body=f'🔺 {STOCK} is UP by {round(percentage_change, 2)}%:\n {show_news()}',
			from_=twil_num, 
			to=my_num
		)
	elif yesterdays_close < (day_before_yd_close*0.95):
		message  = client.messages.create(
			body=f'🔻 {STOCK} is DOWN by {round(percentage_change, 2)}%:\n {show_news()}',
			from_=twil_num, 
			to=my_num
		)
	else:
		message  = client.messages.create(
			body=f'{STOCK} is fairly stable @ {round(percentage_change, 2)}% change:\n {show_news()}',
			from_=twil_num, 
			to=my_num
		)