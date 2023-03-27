from neuralintents import GenericAssistant
import matplotlib.pyplot as plt
import pandas as pd
import pandas_datareader as web
import mplfinance as mpf
import requests
import json
import alpaca_trade_api as tradeapi
import pandas as pd
import numpy as np
import yfinance as yf
import plotly.graph_objs as go
import pickle
import sys
from datetime import datetime,timedelta
import json
from newsapi import NewsApiClient

#For text collection from links:

from newspaper import Article
from newspaper import Config

#For the summarizer:
from transformers import T5ForConditionalGeneration, T5Tokenizer

# for stock sentiment analysis:

# import stocksentimentanalysis as ssa

#Alpaca API Credentials:
api_key = "PKPB8010Q98JE7JHH0Z9"
secret_key = "RXEJsXlXKqPqlXWAcQhw1c3M2OZv5B6bCFRNC1kd"
base_url = 'https://paper-api.alpaca.markets'
endpoint = '/v2/account'

API_KEY = "PKPB8010Q98JE7JHH0Z9"
SECRET_KEY = "RXEJsXlXKqPqlXWAcQhw1c3M2OZv5B6bCFRNC1kd"
APCA_API_BASE_URL = 'https://paper-api.alpaca.markets'


# MY Alpha Vantage API key(Using this for stock details)
api_key_of_alpha_vantage = 'TYPIYSG66KKSZP4J'

# Set headers
headers = {
    "APCA-API-KEY-ID": api_key,
    "APCA-API-SECRET-KEY": secret_key
}

# Initiate the NewsApiClient with your API key
api_key = 'e3cd57bfb8764503acd7d0317b8c0b02'

##function to show the portfolio of a customer:

def show_portfolio():
    api = tradeapi.REST(
          base_url = APCA_API_BASE_URL,
          key_id = API_KEY,
          secret_key = SECRET_KEY
        )
    account = api.get_account()
    if account.trading_blocked:
           message = "Your account is restricted from trading."
        
    else:
         mess = 'Your Trading account Number is: {}'.format(account.account_number)
         mess1 = 'Your portfolio Value is ${}'.format(account.portfolio_value)
         
         mess2 = '${} is available cash for trading.'.format(account.cash)
         mess3 = '${} is available as buying power.'.format(account.buying_power)
         
         total_stock = float(account.portfolio_value) - float(account.cash)
         mess4 = 'Total value of stock available in your porfolio is ${}'.format(total_stock)
         
         balance_change = float(account.equity) - float(account.last_equity)
         mess5 = f'Today portfolio balance changes: ${balance_change}'
         
         message = mess + '\n' + mess1 + '\n' + mess2 + '\n' + mess3 + '\n' + mess4 + '\n' + mess5
    
    print(message)

    account_info = api.get_account()
    positions = api.list_positions()

    stock_data = {}
    
    for position in positions:
        symbol = position.symbol
        
        bars = api.get_bars(symbol, tradeapi.TimeFrame.Day, '2023-01-01', '2023-03-10')
        stock_data[symbol] = bars

    data = []

    for symbol, bars in stock_data.items():
        data.append(
            go.Candlestick(x=[bar.t for bar in bars],
                       open=[bar.o for bar in bars],
                       high=[bar.h for bar in bars],
                       low=[bar.l for bar in bars],
                       close=[bar.c for bar in bars],
                       name=symbol)
        )

    layout = go.Layout(
        title='Portfolio Status',
        yaxis=dict(title='Price in USD($)'),
        xaxis=dict(title='Date')
        )

    fig = go.Figure(data=data, layout=layout)

    fig.show()

# show_portfolio(api_key,secret_key)

##Gives the details of last 5 transactions:

def last_tran_details():
    api = tradeapi.REST(
        base_url = APCA_API_BASE_URL,
        key_id = API_KEY,
        secret_key = SECRET_KEY
    )
      
    message = ''
    last = api.list_orders(status = 'all', limit = 5, direction = 'desc')
      
    for order in last:

        if order.order_type == 'limit':
            mess = 'Transacted At '+ str(order.submitted_at)+ ' '+ order.order_type.capitalize()+ ' order to '+ order.side + ' '+ str(order.qty) + ' stock of '+order.symbol + ' company'+ ' is '+ order.status + ' with limit price of $' + order.limit_price + '.'
        else:
            mess = 'Transacted At '+ str(order.submitted_at)+ ' '+ order.order_type.capitalize() + ' order to ' + order.side+ ' ' + str(order.qty) + ' stock of '+ order.symbol + ' company is ' + order.status+'.'

        message = message + '\n' + mess
    
    print(message)

# last_tran_details(api_key,secret_key)

##Function to get the stock symbol using company name:
def getTicker(company_name):
    yfinance = "https://query2.finance.yahoo.com/v1/finance/search"
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    params = {"q": company_name, "quotes_count": 1, "country": "United States"}

    res = requests.get(url=yfinance, params=params, headers={'User-Agent': user_agent})
    data = res.json()

    company_code = data['quotes'][0]['symbol']
    return company_code

## Function for buying the stocks:

def stock_buy():
    api = tradeapi.REST(
        base_url = APCA_API_BASE_URL,
        key_id = API_KEY,
        secret_key = SECRET_KEY
    )
    
    company = input("Which company stocks you want to buy?")
    company_symbol = getTicker(company)
    amount = input("How many stocks you want to buy?")
    type_of_buying = input("Enter the type of buying (market or limit)")

    if type_of_buying.lower() == 'market':
         order = api.submit_order(symbol = company_symbol, qty = amount, side = 'buy', type = 'market', time_in_force = 'day')

    else:

         lim_price = input("Enter the limit price( in $):")
         order = api.submit_order(symbol = company_symbol, qty = amount, side = 'buy', type = 'limit',limit_price = lim_price, time_in_force = 'day')
    
    print("The task is completed.")

##Function to sell stocks:

def stock_sell():
    api = tradeapi.REST(
        base_url = APCA_API_BASE_URL,
        key_id = API_KEY,
        secret_key = SECRET_KEY
    )
    
    company = input("Which company stocks you want to sell?")
    company_symbol = getTicker(company)
    amount = input("How many stocks you want to sell?")
    type_of_selling = input("Enter the type of selling (Market or Limit)")

    if type_of_selling.lower() == 'market':
         order = api.submit_order(symbol = company_symbol, qty = amount, side = 'sell', type = 'market', time_in_force = 'day')

    else:

         lim_price = input("Enter the limit price( in $):")
         order = api.submit_order(symbol = company_symbol, qty = amount, side = 'sell', type = 'limit',limit_price = lim_price, time_in_force = 'day')
    
    print("The task is completed.")

#Function for stock prices and trends:

def stock_prices():
     api_key = 'TYPIYSG66KKSZP4J'

     company = input("Enter the name of the company: ")
     # Enter the stock symbol you want to retrieve details for
     symbol = getTicker(company)
     # Send a request to the Alpha Vantage API and get the JSON response
     response = requests.get(f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={api_key}')
     data = response.json()
     # Extract the details from the JSON response
     price = data['Global Quote']['05. price']
     open_price = data['Global Quote']['02. open']
     high_price = data['Global Quote']['03. high']
     low_price = data['Global Quote']['04. low']
     volume = data['Global Quote']['06. volume']
     change_percent = data['Global Quote']['10. change percent']
     
     # Print the details
     print(f'Stock Details--------------------------------------------------')
     print(f'Stock Symbol: {symbol}')
     print(f'Price: ${price}')
     print(f'Open Price: ${open_price}')
     print(f'High Price: ${high_price}')
     print(f'Low Price: ${low_price}')
     print(f'Volume: {volume}')
     print(f'Change Percent: {change_percent}')

     data = yf.download(tickers=symbol, period='5d', interval = '1m')
     #declare figure
     fig = go.Figure()
     #Candlestick
     fig.add_trace(go.Candlestick(x=data.index,
                    open=data['Open'],
                    high=data['High'],
                    low=data['Low'],
                    close=data['Close'], name = 'market data'))
     # Add titles
     fig.update_layout(
        title=company + ' live share price evolution',
        yaxis_title='Stock Price (USD per Shares)')
     
     # X-Axes
     fig.update_xaxes(
          rangeslider_visible=True,
          rangeselector=dict(
          buttons=list([
          dict(count=15, label="15m", step="minute", stepmode="backward"),
          dict(count=45, label="45m", step="minute", stepmode="backward"),
          dict(count=1, label="HTD", step="hour", stepmode="todate"),
          dict(count=3, label="3h", step="hour", stepmode="backward"),
          dict(step="all")
          ])
          )
          )
     fig.show()

##Summarizer function:

def ask_and_perform_function_of_summarizer(df):
    while True:
        # Ask the user a question
        answer = input("Do you want summary of any of these articles? ")

        # Check if the user answered "yes"
        if answer.lower() == "yes":
            # Perform the certain function
            summary(df)
        # Check if the user answered "no"
        elif answer.lower() == "no":
            # End the function
            print("Ending the function...")
            break
        # Handle invalid input
        else:
            print("Invalid input, please answer 'yes' or 'no'.")

#The perform function of summarizer:
def summary(df):
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'  ##Yogendra's Machine user_agent
    config = Config()
    config.browser_user_agent = user_agent

    list = []
    for ind in df.index:
        dict1={}
        article = Article(df['URL'][ind], config=config)
        article.download()
        article.parse()
        article.nlp() 
        dict1['Title']=article.title
        dict1['Article']=article.text
        list.append(dict1)
    
    news_df=pd.DataFrame(list)

    ##Loading the summarizer model:

    model = T5ForConditionalGeneration.from_pretrained('saved_model')
    tokenizer = T5Tokenizer.from_pretrained('saved_model')

    ##Taking the user input of the article which he/she wants summary of:

    i = input('Please provide me the row number of the article which you want summary of: ' )
    i = int(i)

    sequence = news_df.iat[i,1]
    inputs = tokenizer.encode('summarize: '+ sequence, return_tensors='pt', max_length = 512, truncation = True)
    outputs = model.generate(inputs,min_length = 80, max_length = 300,length_penalty = 5, num_beams=2)
    summary = tokenizer.decode(outputs[0])
    length = len(summary)
    actual_summary= summary[6:length-4]

    print("Your Summary: "+ actual_summary)

def stock_news():
    newsapi = NewsApiClient(api_key=api_key)
    # Specify the query parameters
    company = input("Enter the name of the company: ")
    query = getTicker(company) # the stock symbol
    language = 'en' # the language of the articles

    #date of 10 days ago or we can change on our own:
    ten_days_ago = datetime.today() - timedelta(days=10)

    # Format the date as a string
    date_string = ten_days_ago.strftime('%Y-%m-%d')

    from_date = date_string # the start date of the articles
     
    # Make the API request
    articles = newsapi.get_everything(q=query, language=language, from_param=from_date)
    df = pd.DataFrame()
    # Print the titles and URLs of the articles
    i=0
    for article in articles['articles']:

        if i==10:
             break
        
        df.loc[i, "Title"] = article['title']
        df.loc[i,"URL"] = article['url']
        i+=1
    print(df)

    ask_and_perform_function_of_summarizer(df)

##The greeting function:
def greetings():
    print("Hello Sir, my name is Harshad Mehta. Your very own stock market advisor and helper.")
##The ending function:
def bye():
     
    print("Goodbye for now. But do remember that Harshad is always there for you.")
    sys.exit(0)

#Function for stock sentiment analysis:
def sentiment_analysis():
    company = input("Enter the name of the company: ")
    symbol = [getTicker(company)]

    ssa.StockSentiment(5,symbol)

# sentiment_analysis()

mappings = {

    'show_portfolio': show_portfolio,
    'last_trans_details': last_tran_details,
    'stock_buy': stock_buy,
    'stock_sell': stock_sell,
    'stock_prices': stock_prices,
    'stock_news': stock_news,
    'greetings': greetings,
    'Bye': bye
}


assistant = GenericAssistant('D:\chatbot_3\money-mavericks\intents.json', mappings, "D:\chatbot_3\money-mavericks\Harshad_Mehta_bot")

#Commands for training and saving the bot model

# assistant.train_model()
# assistant.save_model()

# Command for loading the model:
assistant.load_model()


while True:
    message = input("")
    assistant.request(message)

