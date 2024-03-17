from binance.client import Client
import time
import requests

key="5AciUnbYRHOp3jqFPQDUCqjzrM4Gt6iY9Rk1lK4XbPrDguCDh5FzQCZZd7aEsX1p"
secret="1RBXR8IdgU9Vrk0EGUHL5ELfXAydjUDM9csQH1btme9SLxfl8LpLdaShWYoJ2RE6"


# key="bfcd95fbe7c9f7d49ef50f3eb01d82b80a519138371d7407d76c09269bd3b87f"# TEST
# secret="212bf5426c9902574b0ef25d78b6d6a026d9453a68eba486a595d6c8970178aa"# TEST



client = Client(api_key=key,api_secret=secret)
symbol="CHRUSDT"

#data=client.futures_klines(symbol=symbol,interval=client.KLINE_INTERVAL_1HOUR,limit=3)

#print(data)

# [1710528300000, '70795.20', '70802.70', '70500.00', '70802.70', '297.559', 1710528599999, '21033097.81340', 215, '175.377', '12409893.93880', '0']


data=client.futures_get_open_orders(symbol=symbol)
# for order in data:
#     print(order['status'])
#     print(order['side'])
#     print(order['clientOrderId'])
#     print(order['orderId'])
print(data)

info = client.futures_account()['positions']
openTrades=0
currAmount=0
_entryPrice=0
for obj in info:
    if float(obj['maintMargin'])>0:
        #print(obj)
        openTrades+=1
        currAmount+=float(obj['positionAmt'])
        _entryPrice+=float(obj['entryPrice'])

print(openTrades)



'''
- Need a var to know the start and end of the signal so as not to spam the bot
- Just upload it to the same bot and see how to make it work
'''


# base="https://fapi.binance.com"
# url="/fapi/v1/klines"

# params={"symbol":symbol,"interval":"5m","limit":3}

# data=requests.get(url=base+url,params=params).json()

# #[1710529500000, '0.4111', '0.4114', '0.4069', '0.4101', '725793', 1710529799999, '296625.6913', 2070, '225974', '92436.2031', '0']
# #1 open, 4 close
# #print(data)
# states=[]
# revData=[]
# for candle in data:
#     if float(candle[1])>float(candle[4]):
#         states.append(-1)
#         print("RED")
#     if float(candle[1])<float(candle[4]):
#         states.append(1)
#         print("GREEN")
#     revData.append(candle)
# #print(states)
# #print(revData)
# if states[0]==-1 and states[1]==1:
#     #print(revData[0])
#     #print(revData[1])

#     #redOpen=revData[0][1]
#     #redClose=revData[0][4]

#     greenOpen=float(revData[1][1])
#     greenClose=float(revData[1][4])

#     isSignal=((greenClose-greenOpen)/greenOpen)*100>=0.0002
#     if isSignal:
#         dis=(greenOpen*1.0018) if greenClose<(greenOpen*1.0018) else greenClose
#         zero = (dis-greenOpen*0.786)/(1-0.786)
#         goldenRatio=zero-(zero-greenOpen)*0.618
#         tp=greenClose+(goldenRatio-greenClose)*0.9

#         support1=zero-(zero-greenOpen)*1.618
#         support2=zero-(zero-greenOpen)*2.618
#         support3=zero-(zero-greenOpen)*3.618
#         support4=zero-(zero-greenOpen)*4.5

#         print("{:0.0{}f}".format(float(tp), 4))
#         print("{:0.0{}f}".format(float(support1), 4))
#         print("{:0.0{}f}".format(float(support2), 4))
#         print("{:0.0{}f}".format(float(support3), 4))
#         print("{:0.0{}f}".format(float(support4), 4))
