# Copyright (c) 2024 Jarid Prince

from days.day_036.files.helpers import *


def day_036():
    title("STOCK NOTIFIER")
    load_dotenv()
    TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
    TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
    TWILIO_NUM = os.getenv("TWILIO_NUM")
    MY_PERSONAL_NUMBER = os.getenv("MY_PERSONAL_NUMBER")
    STOCK_KEY = os.getenv("STOCK_KEY")
    NEWS_KEY = os.getenv("NEWS_KEY")

    STOCK = "TSLA"
    COMPANY_NAME = "Tesla"
    FUNCTION = "TIME_SERIES_DAILY"
    # FUNCTION = "TIME_SERIES_INTRADAY"
    今日 = dt.utcnow().date()
    昨日 = 今日 - td(days=1)
    一昨日 = 今日 - td(days=2)

    stock_params = {
        "function": FUNCTION,
        "symbol": STOCK,
        "outputsize": "compact",
        "apikey": STOCK_KEY,
    }
    stock_response = requests.get(
        "https://www.alphavantage.co/query", params=stock_params
    )
    stock_response.raise_for_status()
    データ = stock_response.json()
    print(データ)
    日データ = データ["Time Series (Daily)"]
    昨日のデータ = 日データ[str(昨日)]
    一昨日のデータ = 日データ[str(一昨日)]

    news_params = {
        "apiKey": NEWS_KEY,
        "q": COMPANY_NAME,
        "pageSize": 3,
        "country": "us",
    }

    news_response = requests.get(
        "https://newsapi.org/v2/top-headlines", params=news_params
    )
    news_response.raise_for_status()
    news_data = news_response.json()["articles"]
    if len(news_data) < 3:
        endrange = len(news_data)
    else:
        endrange = 3

    yesterdays_close = float(昨日のデータ["4. close"])
    day_before_yd_close = float(一昨日のデータ["4. close"])
    difference = day_before_yd_close - yesterdays_close
    percentage_change = difference / day_before_yd_close * 100

    articles = {}
    for artnum in range(0, endrange):
        articles[artnum + 1] = {
            "Headline": news_data[artnum]["title"],
            "Brief": news_data[artnum]["description"],
        }

    def show_news():
        news = ""
        for num in articles:
            news += f'\nHeadline: {articles[num]["Headline"]}\nBrief: {articles[num]["Brief"]}\n'
        if news == "":
            return "No news."
        else:
            return news

    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    if yesterdays_close > (day_before_yd_close * 1.05):
        message = client.messages.create(
            body=f"🔺 {STOCK} is UP by {round(percentage_change, 2)}%:\n {show_news()}",
            from_=TWILIO_NUM,
            to=MY_PERSONAL_NUMBER,
        )
    elif yesterdays_close < (day_before_yd_close * 0.95):
        message = client.messages.create(
            body=f"🔻 {STOCK} is DOWN by {round(percentage_change, 2)}%:\n {show_news()}",
            from_=TWILIO_NUM,
            to=MY_PERSONAL_NUMBER,
        )
    else:
        message = client.messages.create(
            body=f"{STOCK} is fairly stable @ {round(percentage_change, 2)}% change:\n {show_news()}",
            from_=TWILIO_NUM,
            to=MY_PERSONAL_NUMBER,
        )
