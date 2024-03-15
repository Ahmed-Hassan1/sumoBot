from binance.client import Client

#key="5AciUnbYRHOp3jqFPQDUCqjzrM4Gt6iY9Rk1lK4XbPrDguCDh5FzQCZZd7aEsX1p"
#secret="1RBXR8IdgU9Vrk0EGUHL5ELfXAydjUDM9csQH1btme9SLxfl8LpLdaShWYoJ2RE6"


test_key="bfcd95fbe7c9f7d49ef50f3eb01d82b80a519138371d7407d76c09269bd3b87f"

test_secret="212bf5426c9902574b0ef25d78b6d6a026d9453a68eba486a595d6c8970178aa"

client = Client(api_key=test_key,api_secret=test_secret,testnet=True)
symbol="CHRUSDT"


data=client.futures_get_open_orders(symbol="ETHUSDT")
for order in data:
    print(order['status'])
    print(order['side'])
    print(order['clientOrderId'])
    print(order['orderId'])
    if float(order['origQty'])<60:
        info=client.futures_cancel_order(symbol="ETHUSDT",clientOrderId=order['clientOrderId'],orderId=order['orderId'])
print(data)