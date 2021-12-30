import ccxt
import os
import pandas as pd
import config
from pprint import pprint

creds = config.CREDENTIALS

exchange_id = 'ftx'
exchange_class = getattr(ccxt, exchange_id)
exchange = exchange_class({
    'apiKey': os.environ['ftx_key'],
    'secret': os.environ['ftx_sec'],
})

previous_timestamp = exchange.milliseconds()
while True:
    try:
        balance = exchange.fetch_balance()
        print('--------------------------------------------------------------')
        current_timestamp = exchange.milliseconds()
        print(exchange.iso8601(current_timestamp), 'balance:')
        pprint(balance)
        print('Fetched in', current_timestamp - previous_timestamp, 'milliseconds')
        previous_timestamp = current_timestamp
    except Exception as e:
        print(type(e).__name__, str(e))

# data = exchange.fetch_balance()
# balance = pd.DataFrame(data['info']['result'], columns=['coin', 'total', 'usdValue'])
# pprint(balance)