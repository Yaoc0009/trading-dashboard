import os
import ccxt

ftx = ccxt.ftx({
    'apiKey': os.environ['ftx_key'],
    'secret': os.environ['ftx_sec'],
})
print(ftx.fetch_balance())