from Bot.models import Entries,TEST
from binance.client import Client
import logging


#TESTING API
# key="bfcd95fbe7c9f7d49ef50f3eb01d82b80a519138371d7407d76c09269bd3b87f"
# secret="212bf5426c9902574b0ef25d78b6d6a026d9453a68eba486a595d6c8970178aa"
# symbol="BTCUSDT"
logger=logging.getLogger("jobs")

key="5AciUnbYRHOp3jqFPQDUCqjzrM4Gt6iY9Rk1lK4XbPrDguCDh5FzQCZZd7aEsX1p"
secret="1RBXR8IdgU9Vrk0EGUHL5ELfXAydjUDM9csQH1btme9SLxfl8LpLdaShWYoJ2RE6"
client = Client(api_key=key,api_secret=secret)
#symbol="CHRUSDT"
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
            if openTrades>0:
                entries=Entries.objects.all().first()
                #info=client.futures_symbol_ticker(symbol=symbol)
                #currentPrice=float(info['price'])
                #print(currentPrice)
                if entries.activateNewEntry==False:

                    info = client.futures_get_order(symbol=symbol,clientOrderId=entries.clientOrderId,orderId=entries.orderId)
                    if info['status']=='FILLED':
                        #info=client.futures_cancel_all_open_orders(symbol=symbol)
                        #print(info)

                        #STOP
                        # data=client.futures_create_order(symbol=symbol, type=Client.FUTURE_ORDER_TYPE_STOP, side=Client.SIDE_SELL, quantity=currAmount*2,stopprice=entries.stop,price=entries.stop)
                        # print(data)

                        #Profit
                        try:
                            
                            logger.info("Cancel 1")
                            logger.info(_entryPrice)
                            qty=int(float(entries.entryQuant))+int(float(entries.newEntryQuant))
                            try:
                                data=client.futures_get_open_orders(symbol=symbol)
                                for order in data:
                                    logger.info(order['status'])
                                    logger.info(order['side'])
                                    logger.info(order['clientOrderId'])
                                    logger.info(order['orderId'])
                                    if float(order['origQty'])<qty:
                                        info=client.futures_cancel_order(symbol=symbol,clientOrderId=order['clientOrderId'],orderId=order['orderId'])
                                        logger.info(info)
                            except Exception as e:
                                logger.error(e)
                            #nT="{:0.0{}f}".format(float(entries.targetDist)+_entryPrice, price_precision)
                            #data=client.futures_create_order(symbol=symbol, type=Client.FUTURE_ORDER_TYPE_LIMIT, side=Client.SIDE_SELL, quantity=qty,price=entries.newTarget,timeinforce=Client.TIME_IN_FORCE_GTC)
                            logger.info("SENDING P1")
                            data=client.futures_create_order(symbol=symbol, type=Client.FUTURE_ORDER_TYPE_LIMIT, side=Client.SIDE_SELL, quantity=qty,price=entries.newTarget,limitprice=entries.newTarget,timeinforce=Client.TIME_IN_FORCE_GTC)
                            logger.info(data)
                            entries.activateNewEntry=True
                            entries.targetClientId=data['clientOrderId']
                            entries.targetOrderId=data['orderId']
                            entries.save()
                            logger.info("DONE P1")
                        except Exception as e:
                            logger.error("ERROR 1")
                            logger.error(e)
                        

                if entries.activateNewEntry2==False:

                    info = client.futures_get_order(symbol=symbol,clientOrderId=entries.clientOrderId2,orderId=entries.orderId2)

                    if info['status']=='FILLED':
                        #info=client.futures_cancel_all_open_orders(symbol=symbol)
                        #print(info)

                        #STOP 
                        # data=client.futures_create_order(symbol=symbol, type=Client.FUTURE_ORDER_TYPE_STOP, side=Client.SIDE_SELL, quantity=currAmount*2,stopprice=entries.stop,price=entries.stop)
                        # print(data)

                        #Profit
                        try:
                            
                            logger.info("Cancel 2")
                            logger.info(_entryPrice)
                            qty=int(float(entries.entryQuant))+int(float(entries.newEntryQuant))+int(float(entries.newEntryQuant2))
                            try:
                                data=client.futures_get_open_orders(symbol=symbol)
                                for order in data:
                                    logger.info(order['status'])
                                    logger.info(order['side'])
                                    logger.info(order['clientOrderId'])
                                    logger.info(order['orderId'])
                                    if float(order['origQty'])<qty:
                                        info=client.futures_cancel_order(symbol=symbol,clientOrderId=order['clientOrderId'],orderId=order['orderId'])
                                        logger.info(info)
                            except Exception as e:
                                logger.error(e)
                            #nT="{:0.0{}f}".format(float(entries.targetDist)+_entryPrice, price_precision)
                            #data=client.futures_create_order(symbol=symbol, type=Client.FUTURE_ORDER_TYPE_LIMIT, side=Client.SIDE_SELL, quantity=qty,price=nT,timeinforce=Client.TIME_IN_FORCE_GTC)
                            logger.info("SENDING P2")
                            data=client.futures_create_order(symbol=symbol, type=Client.FUTURE_ORDER_TYPE_LIMIT, side=Client.SIDE_SELL, quantity=qty,price=entries.newTarget2,limitprice=entries.newTarget2,timeinforce=Client.TIME_IN_FORCE_GTC)
                            logger.info(data)
                            entries.targetClientId2=data['clientOrderId']
                            entries.targetOrderId2=data['orderId']
                            entries.activateNewEntry2=True
                            entries.save()
                            logger.info("DONE P2")
                        except Exception as e:
                            logger.error("ERROR 2")
                            logger.error(e)
                        

                if entries.activateNewEntry3==False:

                    info = client.futures_get_order(symbol=symbol,clientOrderId=entries.clientOrderId3,orderId=entries.orderId3)

                    if info['status']=='FILLED':
                        #info=client.futures_cancel_all_open_orders(symbol=symbol)
                        #print(info)

                        #STOP
                        # data=client.futures_create_order(symbol=symbol, type=Client.FUTURE_ORDER_TYPE_STOP, side=Client.SIDE_SELL, quantity=currAmount*2,stopprice=entries.stop,price=entries.stop)
                        # print(data)

                        #Profit
                        try:
                            logger.info("Cancel 3")
                            logger.info(_entryPrice)
                            qty=int(float(entries.entryQuant))+int(float(entries.newEntryQuant))+int(float(entries.newEntryQuant2))+int(float(entries.newEntryQuant3))
                            try:
                                data=client.futures_get_open_orders(symbol=symbol)
                                for order in data:
                                    logger.info(order['status'])
                                    logger.info(order['side'])
                                    logger.info(order['clientOrderId'])
                                    logger.info(order['orderId'])
                                    if float(order['origQty'])<qty:
                                        info=client.futures_cancel_order(symbol=symbol,clientOrderId=order['clientOrderId'],orderId=order['orderId'])
                                        logger.info(info)
                            except Exception as e:
                                logger.error(e)
                            #nT="{:0.0{}f}".format(float(entries.targetDist)+_entryPrice, price_precision)
                            #data=client.futures_create_order(symbol=symbol, type=Client.FUTURE_ORDER_TYPE_LIMIT, side=Client.SIDE_SELL, quantity=qty,price=nT,timeinforce=Client.TIME_IN_FORCE_GTC)
                            logger.info("SENDING P3")
                            data=client.futures_create_order(symbol=symbol, type=Client.FUTURE_ORDER_TYPE_LIMIT, side=Client.SIDE_SELL, quantity=qty,price=entries.newTarget3,limitprice=entries.newTarget3,timeinforce=Client.TIME_IN_FORCE_GTC)
                            logger.info(data)
                            entries.targetClientId3=data['clientOrderId']
                            entries.targetOrderId3=data['orderId']
                            entries.activateNewEntry3=True
                            entries.save()
                            logger.info("DONE P3")
                        except Exception as e:
                            logger.error("ERROR 3")
                            logger.error(e)
           

                if entries.activateNewEntry4==False:

                    info = client.futures_get_order(symbol=symbol,clientOrderId=entries.clientOrderId4,orderId=entries.orderId4)

                    if info['status']=='FILLED':
                    
                        #info=client.futures_cancel_all_open_orders(symbol=symbol)
                        #print(info)

                        #STOP
                        # data=client.futures_create_order(symbol=symbol, type=Client.FUTURE_ORDER_TYPE_STOP, side=Client.SIDE_SELL, quantity=currAmount*2,stopprice=entries.stop,price=entries.stop)
                        # print(data)

                        #Profit
                        try:
                            logger.info("Cancel 4")
                            logger.info(_entryPrice)
                            qty=int(float(entries.entryQuant))+int(float(entries.newEntryQuant))+int(float(entries.newEntryQuant2))+int(float(entries.newEntryQuant3))+int(float(entries.newEntryQuant4))
                            try:
                                data=client.futures_get_open_orders(symbol=symbol)
                                for order in data:
                                    logger.info(order['status'])
                                    logger.info(order['side'])
                                    logger.info(order['clientOrderId'])
                                    logger.info(order['orderId'])
                                    if float(order['origQty'])<qty:
                                        info=client.futures_cancel_order(symbol=symbol,clientOrderId=order['clientOrderId'],orderId=order['orderId'])
                                        logger.info(info)
                            except Exception as e:
                                logger.error(e)
                            #nT="{:0.0{}f}".format(float(entries.targetDist)+_entryPrice, price_precision)
                            #data=client.futures_create_order(symbol=symbol, type=Client.FUTURE_ORDER_TYPE_LIMIT, side=Client.SIDE_SELL, quantity=qty,price=nT,timeinforce=Client.TIME_IN_FORCE_GTC)
                            logger.info("SENDING P4")
                            data=client.futures_create_order(symbol=symbol, type=Client.FUTURE_ORDER_TYPE_LIMIT, side=Client.SIDE_SELL, quantity=qty,price=entries.newTarget4,limitprice=entries.newTarget4,timeinforce=Client.TIME_IN_FORCE_GTC)
                            logger.info(data)
                            entries.targetClientId4=data['clientOrderId']
                            entries.targetOrderId4=data['orderId']
                            entries.activateNewEntry4=True
                            entries.save()
                            logger.info("DONE P4")
                        except Exception as e:
                            logger.error("ERROR 4")
                            logger.error(e)
            else:
                client.futures_cancel_all_open_orders(symbol=symbol) 
                #print(1)
                #print(info)  
                isRunning.running=False
                isRunning.save()
        except Exception as e:
            logger.error("GENERAL JOBS ERROR")

            logger.error(e)



def job_2():

    if True:
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
            if openTrades==0:
                client.futures_cancel_all_open_orders(symbol=symbol)
                
        except Exception as e:
            logger.error("GENERAL JOBS ERROR")

            logger.error(e)
