from Bot.models import Entries,TEST
import requests
from binance.client import Client



key="5AciUnbYRHOp3jqFPQDUCqjzrM4Gt6iY9Rk1lK4XbPrDguCDh5FzQCZZd7aEsX1p"
secret="1RBXR8IdgU9Vrk0EGUHL5ELfXAydjUDM9csQH1btme9SLxfl8LpLdaShWYoJ2RE6"
client = Client(api_key=key,api_secret=secret)
symbol="CHRUSDT"
price_precision=4
def job_1():
    isRunning=TEST.objects.all().first()
    
    if isRunning.running:
        try:
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
            #print(openTrades)
            if openTrades>0:
                entries=Entries.objects.all().first()
                #info=client.futures_symbol_ticker(symbol=symbol)
                #currentPrice=float(info['price'])
                #print(currentPrice)
                if entries.activateNewEntry==False:

                    info = client.futures_get_order(symbol=symbol,clientOrderId=entries.clientOrderId,orderId=entries.orderId)
                    #print(info['status'])
                    #print(info['status']=='FILLED')
                    if info['status']=='FILLED':
                        #info=client.futures_cancel_all_open_orders(symbol=symbol)
                        #print(info)

                        #STOP
                        # data=client.futures_create_order(symbol=symbol, type=Client.FUTURE_ORDER_TYPE_STOP, side=Client.SIDE_SELL, quantity=currAmount*2,stopprice=entries.stop,price=entries.stop)
                        # print(data)

                        #Profit
                        try:
                            info=client.futures_cancel_order(symbol=symbol,clientOrderId=entries.targetClientIdBase,orderId=entries.targetOrderIdBase)
                            print("Canceleed")
                            print(info)
                            qty=int(float(entries.entryQuant))+int(float(entries.newEntryQuant))
                            nT="{:0.0{}f}".format(float(entries.targetDist)+_entryPrice, price_precision)
                            data=client.futures_create_order(symbol=symbol, type=Client.FUTURE_ORDER_TYPE_LIMIT, side=Client.SIDE_SELL, quantity=qty,price=nT,timeinforce=Client.TIME_IN_FORCE_GTC)
                            print(data)
                            entries.activateNewEntry=True
                            entries.targetClientId=data['clientOrderId']
                            entries.targetOrderId=data['orderId']
                            entries.save()
                        except Exception as e:
                            print("ERROR 1")
                            print(e)
                        

                elif entries.activateNewEntry2==False:

                    info = client.futures_get_order(symbol=symbol,clientOrderId=entries.clientOrderId2,orderId=entries.orderId2)

                    if info['status']=='FILLED':
                        #info=client.futures_cancel_all_open_orders(symbol=symbol)
                        #print(info)

                        #STOP 
                        # data=client.futures_create_order(symbol=symbol, type=Client.FUTURE_ORDER_TYPE_STOP, side=Client.SIDE_SELL, quantity=currAmount*2,stopprice=entries.stop,price=entries.stop)
                        # print(data)

                        #Profit
                        try:
                            info=client.futures_cancel_order(symbol=symbol,clientOrderId=entries.targetClientId,orderId=entries.targetOrderId)
                            print("Canceleed")
                            print(info)
                            qty=int(float(entries.entryQuant))+int(float(entries.newEntryQuant))+int(float(entries.newEntryQuant2))
                            nT="{:0.0{}f}".format(float(entries.targetDist)+_entryPrice, price_precision)
                            data=client.futures_create_order(symbol=symbol, type=Client.FUTURE_ORDER_TYPE_LIMIT, side=Client.SIDE_SELL, quantity=qty,price=nT,timeinforce=Client.TIME_IN_FORCE_GTC)
                            print(data)
                            entries.targetClientId2=data['clientOrderId']
                            entries.targetOrderId2=data['orderId']
                            entries.activateNewEntry2=True
                            entries.save()
                        except Exception as e:
                            print("ERROR 2")
                            print(e)
                        

                elif entries.activateNewEntry3==False:

                    info = client.futures_get_order(symbol=symbol,clientOrderId=entries.clientOrderId3,orderId=entries.orderId3)

                    if info['status']=='FILLED':
                        #info=client.futures_cancel_all_open_orders(symbol=symbol)
                        #print(info)

                        #STOP
                        # data=client.futures_create_order(symbol=symbol, type=Client.FUTURE_ORDER_TYPE_STOP, side=Client.SIDE_SELL, quantity=currAmount*2,stopprice=entries.stop,price=entries.stop)
                        # print(data)

                        #Profit
                        try:
                            info=client.futures_cancel_order(symbol=symbol,clientOrderId=entries.targetClientId2,orderId=entries.targetOrderId2)
                            print("Canceleed")
                            print(info)
                            qty=int(float(entries.entryQuant))+int(float(entries.newEntryQuant))+int(float(entries.newEntryQuant2))+int(float(entries.newEntryQuant3))
                            nT="{:0.0{}f}".format(float(entries.targetDist)+_entryPrice, price_precision)
                            data=client.futures_create_order(symbol=symbol, type=Client.FUTURE_ORDER_TYPE_LIMIT, side=Client.SIDE_SELL, quantity=qty,price=nT,timeinforce=Client.TIME_IN_FORCE_GTC)
                            print(data)
                            entries.targetClientId3=data['clientOrderId']
                            entries.targetOrderId3=data['orderId']
                            entries.activateNewEntry3=True
                            entries.save()
                        except Exception as e:
                            print("ERROR 3")
                            print(e)

                        

                elif entries.activateNewEntry4==False:

                    info = client.futures_get_order(symbol=symbol,clientOrderId=entries.clientOrderId4,orderId=entries.orderId4)

                    if info['status']=='FILLED':
                    
                        #info=client.futures_cancel_all_open_orders(symbol=symbol)
                        #print(info)

                        #STOP
                        # data=client.futures_create_order(symbol=symbol, type=Client.FUTURE_ORDER_TYPE_STOP, side=Client.SIDE_SELL, quantity=currAmount*2,stopprice=entries.stop,price=entries.stop)
                        # print(data)

                        #Profit
                        try:
                            info=client.futures_cancel_order(symbol=symbol,clientOrderId=entries.targetClientId3,orderId=entries.targetOrderId3)
                            print("Canceleed")
                            print(info)
                            qty=int(float(entries.entryQuant))+int(float(entries.newEntryQuant))+int(float(entries.newEntryQuant2))+int(float(entries.newEntryQuant3))+int(float(entries.newEntryQuant4))
                            nT="{:0.0{}f}".format(float(entries.targetDist)+_entryPrice, price_precision)
                            data=client.futures_create_order(symbol=symbol, type=Client.FUTURE_ORDER_TYPE_LIMIT, side=Client.SIDE_SELL, quantity=qty,price=nT,timeinforce=Client.TIME_IN_FORCE_GTC)
                            print(data)
                            entries.targetClientId4=data['clientOrderId']
                            entries.targetOrderId4=data['orderId']
                            entries.activateNewEntry4=True
                            entries.save()
                        except Exception as e:
                            print("ERROR 4")
                            print(e)
                        

                
                entries.save()
            else:
                client.futures_cancel_all_open_orders(symbol=symbol) 
                #print(1)
                #print(info)  
                isRunning.running=False
                isRunning.save()
        except Exception as e:
            x=1
            print(e)

        
        


def testJob():
    isRunning=TEST.objects.all().first()
    
    if isRunning.running:
        print("RUNNING")
    else:
        print("STOPPED")
