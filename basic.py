import alpaca_trade_api as tradeapi 
import requests
import json
import pandas as pd
from transformers import T5ForConditionalGeneration, T5Tokenizer


API_KEY = "PKY1OGC9DGEWHVCUHIUW"
SECRET_KEY = "kbnjQfQd7guKk2YZMdmxBbWLkMa7Nk3KIUv0zirH"
APCA_API_BASE_URL = 'https://paper-api.alpaca.markets'

api = tradeapi.REST(
   base_url = APCA_API_BASE_URL,
   key_id = API_KEY,
   secret_key = SECRET_KEY
  )

# # account = api.get_account()

# # if account.trading_blocked:
# #     message = "Your account is restricted ffrom trading."

# # else:
# #     mess = 'Your Trading account Number is: {}'.format(account.account_number)
# #     mess1 = 'Your portfolio Value is ${}'.format(account.portfolio_value)

# #     mess2 = '${} is available cash for trading.'.format(account.cash)
# #     mess3 = '${} is available as buying power.'.format(account.buying_power)

# #     total_stock = float(account.portfolio_value) - float(account.cash)
# #     mess4 = 'Total value of stock available in your porfolio is ${}'.format(total_stock)

# #     balance_change = float(account.equity) - float(account.last_equity)
# #     mess5 = f'Today portfolio balance changes: ${balance_change}'

# #     message = mess + '\n' + mess1 + '\n' + mess2 + '\n' + mess3 + '\n' + mess4 + '\n' + mess5

# # print(message)

# import requests

# # Alpha Vantage API endpoint for searching companies
# search_endpoint = "https://www.alphavantage.co/query"

# # Your Alpha Vantage API key
# api_key = "TYPIYSG66KKSZP4J"

# # The company name you want to search for
# company_name = "Microsoft"

# # Parameters for the API request
# params = {
#     "function": "SYMBOL_SEARCH",
#     "keywords": company_name,
#     "apikey": api_key
# }

# # Send the API request
# response = requests.get(search_endpoint, params=params)

# # Extract the symbol from the response
# symbol = response.json()["bestMatches"][0]["1. symbol"]

# # Print the symbol
# print(f"The symbol for {company_name} is {symbol}.")

# from newsapi import NewsApiClient

# # Initiate the NewsApiClient with your API key
# api_key = 'e3cd57bfb8764503acd7d0317b8c0b02'
# newsapi = NewsApiClient(api_key=api_key)

# # Specify the query parameters
# query = 'AAPL' # the stock symbol
# language = 'en' # the language of the articles
# from_date = '2023-03-11' # the start date of the articles

# # Make the API request
# articles = newsapi.get_everything(q=query, language=language, from_param=from_date)

# df = pd.DataFrame()
# print(df)
#  # Print the titles and URLs of the articles

# i=0
# for article in articles['articles']:
#   df.loc[i, "Title"] = article['title']
#   df.loc[i,"URL"] = article['url']
#   i+=1
# print(df)

model = T5ForConditionalGeneration.from_pretrained('t5-base')
tokenizer = T5Tokenizer.from_pretrained('t5-base')

# Save the model and tokenizer
model.save_pretrained('saved_model')
tokenizer.save_pretrained('saved_model')

# Load the saved model and tokenizer
model = T5ForConditionalGeneration.from_pretrained('saved_model')
tokenizer = T5Tokenizer.from_pretrained('saved_model')