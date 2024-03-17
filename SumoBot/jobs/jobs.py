from Bot.models import Entries,TEST
from binance.client import Client
import logging
import requests

logger=logging.getLogger("jobs")

key="5AciUnbYRHOp3jqFPQDUCqjzrM4Gt6iY9Rk1lK4XbPrDguCDh5FzQCZZd7aEsX1p"
secret="1RBXR8IdgU9Vrk0EGUHL5ELfXAydjUDM9csQH1btme9SLxfl8LpLdaShWYoJ2RE6"
client = Client(api_key=key,api_secret=secret)
symbol="CHRUSDT"
price_precision=4
def job_1():
    isRunning=TEST.objects.all().first()
    
    if False:#isRunning.running:
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


def FutureIndicatorFourSupport():
    base="https://fapi.binance.com"
    url="/fapi/v1/klines"

    params={"symbol":symbol,"interval":"5m","limit":3}

    data=requests.get(url=base+url,params=params).json()

    #[1710529500000, '0.4111', '0.4114', '0.4069', '0.4101', '725793', 1710529799999, '296625.6913', 2070, '225974', '92436.2031', '0']
    #1 open, 4 close
    logger.info("Raw Data")
    logger.info(data)
    states=[]
    revData=[]
    for candle in data:
        if float(candle[1])>float(candle[4]):
            states.append(-1)
            #logger.info("RED")
        if float(candle[1])<float(candle[4]):
            states.append(1)
            #logger.info("GREEN")
        if float(candle[1])==float(candle[4]):
            states.append(0)
        revData.append(candle)
    logger.info("Signal")
    logger.info(states)
    logger.info(revData)
    try:
        if states[1]==-1 and states[2]==1:
            #print(revData[0])
            #print(revData[1])

            #redOpen=revData[0][1]
            #redClose=revData[0][4]

            greenOpen=float(revData[2][1])
            greenClose=float(revData[2][4])

            isSignal=((greenClose-greenOpen)/greenOpen)*100>=0.0002
            if isSignal:
                dis=(greenOpen*1.0018) if greenClose<(greenOpen*1.0018) else greenClose
                zero = (dis-greenOpen*0.786)/(1.0-0.786)
                goldenRatio=zero-(zero-greenOpen)*0.618
                tp=greenClose+(goldenRatio-greenClose)*0.9

                support1=zero-(zero-greenOpen)*1.618
                support2=zero-(zero-greenOpen)*2.618
                support3=zero-(zero-greenOpen)*3.618
                support4=zero-(zero-greenOpen)*4.5

                distance=float(tp)-float(greenClose)
                logger.info("LEVELS")
                logger.info("TP: "+"{:0.0{}f}".format(float(tp), 4))
                logger.info("S1: "+"{:0.0{}f}".format(float(support1), 4))
                logger.info("S2: "+"{:0.0{}f}".format(float(support2), 4))
                logger.info("S3: "+"{:0.0{}f}".format(float(support3), 4))
                logger.info("S4: "+"{:0.0{}f}".format(float(support4), 4))
                logger.info("DS: "+"{:0.0{}f}".format(float(distance), 4))

                SignalParams={

                    "distance":distance,
                    "New Entry":support1,
                    "New Entry 2":support2,
                    "New Entry 3":support3,
                    "New Entry 4":support4,
                }
                requests.get("http://127.0.0.1:8000/bot/firstbot",params=SignalParams)
    except Exception as e:
        logger.error(e)