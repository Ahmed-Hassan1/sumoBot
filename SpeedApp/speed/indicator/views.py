from django.shortcuts import render
from django.http import HttpResponse
import time
from binance.client import Client

# Create your views here.

def ticker(request):

    test_key="bfcd95fbe7c9f7d49ef50f3eb01d82b80a519138371d7407d76c09269bd3b87f"

    test_secret="212bf5426c9902574b0ef25d78b6d6a026d9453a68eba486a595d6c8970178aa"

    client = Client(api_key=test_key,api_secret=test_secret,testnet=True)
    symbol="BTCUSDT"

    time.asctime()

    info=client.futures_symbol_ticker(symbol=symbol)
    print(info)

    return HttpResponse("Hello")