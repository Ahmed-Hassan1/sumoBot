from django.http import JsonResponse
from binance.client import Client
from django.views.decorators.csrf import csrf_exempt
import json
from .models import *
import logging

logger=logging.getLogger("views")

key="5AciUnbYRHOp3jqFPQDUCqjzrM4Gt6iY9Rk1lK4XbPrDguCDh5FzQCZZd7aEsX1p"
secret="1RBXR8IdgU9Vrk0EGUHL5ELfXAydjUDM9csQH1btme9SLxfl8LpLdaShWYoJ2RE6"
client = Client(api_key=key,api_secret=secret)
symbol="CHRUSDT"
price_precision=4
BaseOrderSize=6 # number %
@csrf_exempt
def FirstBot(request):
    #FINAL CODE
    try:
        #Check for open entries
        profit=0
        try:
            info = client.futures_account()['positions']
            openTrades=0
            for obj in info:
                if float(obj['maintMargin'])>0:
                    logger.info(obj['unrealizedProfit'])
                    openTrades+=1
                    profit+=float(obj['unrealizedProfit'])
            if openTrades==0:
                #Get different messages
                msg=dict(request.GET)['txt'][0]
                msgJson=json.loads(msg)
                #msgJson=json.loads('{"Entry": "0.4239","Target": "65000","Stop": "50000","New Entry": "59000","New Target": "61000"}')

                #Parse the message to get individual 
                info=client.futures_symbol_ticker(symbol=symbol)
                currentPrice=info['price']
                logger.info("Price: "+str(currentPrice))


                entry=currentPrice
                targetDistance=msgJson['distance']
                target=addTargetToEntries(entry,entry,targetDistance)
                
                logger.info("LOGGING")
                logger.info(entry)
                logger.info(target)


                newEntry= msgJson['New Entry']
                newTarget=addTargetToEntries(entry,newEntry,targetDistance)
                logger.info(newEntry)
                logger.info(newTarget)

                _oldEntry=(float(entry)+float(newEntry))/2
                oldEntry="{:0.0{}f}".format(float(_oldEntry), price_precision)
                newEntry2=msgJson['New Entry 2']
                newTarget2=addTargetToEntries(oldEntry,newEntry2,targetDistance)
                logger.info(newEntry2)
                logger.info(newTarget2)

                _oldEntry2=(float(_oldEntry)+float(newEntry2))/2
                oldEntry2="{:0.0{}f}".format(float(_oldEntry2), price_precision)
                newEntry3=msgJson['New Entry 3']
                newTarget3=addTargetToEntries(oldEntry2,newEntry3,targetDistance)
                logger.info(newEntry3)
                logger.info(newTarget3)

                _oldEntry3=(float(_oldEntry2)+float(newEntry3))/2
                oldEntry3="{:0.0{}f}".format(float(_oldEntry3), price_precision)
                newEntry4=msgJson['New Entry 4']
                newTarget4=addTargetToEntries(oldEntry3,newEntry4,targetDistance)
                logger.info(newEntry4)
                logger.info(newTarget4)

                #Save to DB
                entries=Entries.objects.all().first()
                if not entries:
                    entries=Entries.objects.create(
                        entry=entry,
                        target=target,
                        #stop=stop,
                        newEntry=newEntry,
                        newTarget=newTarget,
                        newEntry2=newEntry2,
                        newTarget2=newTarget2,
                        newEntry3=newEntry3,
                        newTarget3=newTarget3,
                        newEntry4=newEntry4,
                        newTarget4=newTarget4,
                        targetDist=targetDistance)
                else:
                    #entries=Entries.objects.all().first()
                    entries.entry="{:0.0{}f}".format(float(entry), price_precision)
                    entries.target="{:0.0{}f}".format(float(target), price_precision)
                    #entries.stop="{:0.0{}f}".format(float(stop), price_precision)

                    entries.newEntry="{:0.0{}f}".format(float(newEntry), price_precision)
                    entries.newTarget="{:0.0{}f}".format(float(newTarget), price_precision)

                    entries.newEntry2="{:0.0{}f}".format(float(newEntry2), price_precision)
                    entries.newTarget2="{:0.0{}f}".format(float(newTarget2), price_precision)

                    entries.newEntry3="{:0.0{}f}".format(float(newEntry3), price_precision)
                    entries.newTarget3="{:0.0{}f}".format(float(newTarget3), price_precision)

                    entries.newEntry4="{:0.0{}f}".format(float(newEntry4), price_precision)
                    entries.newTarget4="{:0.0{}f}".format(float(newTarget4), price_precision)
                    entries.targetDist=targetDistance
                    entries.save()

                


                entries.activateNewEntry=False
                entries.activateNewEntry2=False
                entries.activateNewEntry3=False
                entries.activateNewEntry4=False
                entries.save()
                #check last closed order
                info=client.futures_account_trades(symbol=symbol)
                if len(info)>0 and float(info[len(info)-1]['realizedPnl'])<0:
                    entries.currentLeverage=entries.currentLeverage*2
                else:
                    entries.currentLeverage=entries.baseLeverage
                entries.save()

                #Calculte QTY
                acc_balance = client.futures_account_balance()
                quantity=0
                quantity1=0
                quantity2=0
                quantity3=0
                quantity4=0
                balance=0
                for check_balance in acc_balance:
                    if check_balance["asset"] == "USDT":
                        usdt_balance = check_balance["balance"]
                        balance+=float(usdt_balance)
                        info=client.futures_symbol_ticker(symbol=symbol)
                        currentPrice=float(info['price'])

                        usdt=int(float(usdt_balance))*BaseOrderSize/100
                        quantity+=int(float(usdt/currentPrice))

                        usdt=int(float(usdt_balance))*BaseOrderSize/100
                        quantity1+=int(float(usdt/float(entries.newEntry)))

                        usdt=int(float(usdt_balance))*BaseOrderSize*2/100
                        quantity2+=int(float(usdt/float(entries.newEntry2)))

                        usdt=int(float(usdt_balance))*BaseOrderSize*4/100
                        quantity3+=int(float(usdt/float(entries.newEntry3)))

                        usdt=int(float(usdt_balance))*BaseOrderSize*8/100
                        quantity4+=int(float(usdt/float(entries.newEntry4)))
                        #quantity = "{:0.0{}f}".format(quantity, 1)
                        #quantity
                        logger.info(usdt_balance)
                        logger.info(usdt)
                        logger.info("QTY: "+quantity.__str__()+"  "+quantity1.__str__()+"  "+quantity2.__str__()+"  "+quantity3.__str__()+"  "+quantity4.__str__())
                #change Margin Type
                try:
                    info = client.futures_change_margin_type(symbol=symbol,marginType='ISOLATED')
                    logger.info(info)
                except Exception as e:
                    logger.info("1"+e.__str__())
                #change leverage
                try:
                    #info = client.futures_change_leverage(symbol=symbol,leverage=entries.currentLeverage)
                    info = client.futures_change_leverage(symbol=symbol,leverage=1)
                    logger.info(info)
                except Exception as e:
                    logger.info("2"+e.__str__())
                #Single Asset Mode checker
                try:
                    info=client.futures_get_multi_assets_mode()
                    logger.info(info)
                except Exception as e:
                    logger.info("3"+e.__str__())
                #Position Mode
                try:
                    info = client.futures_change_position_mode(dualSidePosition="false")
                    logger.info(info)
                except Exception as e:
                    logger.info("4"+e.__str__())


                logger.info("No Open Trades for current Symbol")
                if balance>=100:
                    try:
                        #Entry
                        logger.info("Entry")
                        
                        data=client.futures_create_order(symbol=symbol, type=Client.FUTURE_ORDER_TYPE_MARKET, side=Client.SIDE_BUY, quantity=quantity)
                        entries.entryQuant=quantity
                        entries.entryClientId=data['clientOrderId']
                        entries.entryOrderId=data['orderId']
                        entries.save()
                        
                        logger.info(data)
                    except Exception as e:
                        logger.info("ENTRY")
                        logger.info(e)

                    # try: 
                    #     #STOP
                    #     data=client.futures_create_order(symbol=symbol, type=Client.FUTURE_ORDER_TYPE_STOP, side=Client.SIDE_SELL, quantity=quantity,stopprice=entries.stop,price=entries.stop)
                    #     logger.info("Stop")
                    #     logger.info(data)
                    #     logger.info(quantity)
                    # except Exception as e:
                    #     logger.info("STOP")
                    #     logger.info(e)

                    try:
                        #Profit
                        logger.info("Profit")
                        info = client.futures_get_order(symbol=symbol,clientOrderId=entries.entryClientId,orderId=entries.entryOrderId)
                        logger.info(info['avgPrice'])
                        starterProfit=addTargetToEntries(info['avgPrice'],info['avgPrice'],entries.targetDist)

                        data=client.futures_create_order(symbol=symbol, type=Client.FUTURE_ORDER_TYPE_LIMIT, side=Client.SIDE_SELL, quantity=quantity,price=starterProfit,limitprice=starterProfit,timeinforce=Client.TIME_IN_FORCE_GTC)
                        
                        entries.targetClientIdBase=data['clientOrderId']
                        entries.targetOrderIdBase=data['orderId']

                        logger.info(data)
                    except Exception as e:
                        logger.info("PROFIT")
                        logger.info(e)

                    try:
                        #NEW ENTRY
                        logger.info("new Entry")

                        data=client.futures_create_order(symbol=symbol, type=Client.FUTURE_ORDER_TYPE_LIMIT, side=Client.SIDE_BUY, quantity=quantity1,price=entries.newEntry,limitprice=entries.newEntry,timeinforce=Client.TIME_IN_FORCE_GTC)

                        entries.clientOrderId=data['clientOrderId']
                        entries.orderId=data['orderId']
                        entries.newEntryQuant=quantity1

                        logger.info(data)
                        
                    except Exception as e:
                        logger.info("NEW ENTRY")
                        logger.info(e)

                    try:
                        #NEW ENTRY 2
                        logger.info("new Entry 2")

                        data=client.futures_create_order(symbol=symbol, type=Client.FUTURE_ORDER_TYPE_LIMIT, side=Client.SIDE_BUY, quantity=quantity2,price=entries.newEntry2,limitprice=entries.newEntry2,timeinforce=Client.TIME_IN_FORCE_GTC)

                        entries.clientOrderId2=data['clientOrderId']
                        entries.orderId2=data['orderId']
                        entries.newEntryQuant2=quantity2

                        logger.info(data)
                        
                    except Exception as e:
                        logger.info("NEW ENTRY 2")
                        logger.info(e)

                    try:
                        #NEW ENTRY 3
                        logger.info("new Entry 3")

                        data=client.futures_create_order(symbol=symbol, type=Client.FUTURE_ORDER_TYPE_LIMIT, side=Client.SIDE_BUY, quantity=quantity3,price=entries.newEntry3,limitprice=entries.newEntry3,timeinforce=Client.TIME_IN_FORCE_GTC)

                        entries.clientOrderId3=data['clientOrderId']
                        entries.orderId3=data['orderId']
                        entries.newEntryQuant3=quantity3

                        logger.info(data)
                        
                    except Exception as e:
                        logger.info("NEW ENTRY 3")
                        logger.info(e)

                    try:
                        #NEW ENTRY 4
                        logger.info("new Entry 4")

                        data=client.futures_create_order(symbol=symbol, type=Client.FUTURE_ORDER_TYPE_LIMIT, side=Client.SIDE_BUY, quantity=quantity4,price=entries.newEntry4,limitprice=entries.newEntry4,timeinforce=Client.TIME_IN_FORCE_GTC)

                        entries.clientOrderId4=data['clientOrderId']
                        entries.orderId4=data['orderId']
                        entries.newEntryQuant4=quantity4
                        
                        logger.info(data)
                        isRunning=TEST.objects.all().first()
                        isRunning.running=True
                        isRunning.save()
                        
                    except Exception as e:
                        logger.info("NEW ENTRY 4")
                        logger.info(e)

        except Exception as e:
            logger.error(e)

        entries.save()
    except Exception as e:
        logger.error(e)

    return JsonResponse({"PnL":1},safe=False)
    


def targetModify(tp,entry):
    tp=float(tp)
    price=float(entry)
    perc=tp/price-1
    newPerc=perc if perc>=0.0012 else 0.0012
    newT=price*newPerc
    return "{:0.0{}f}".format(float(newT), price_precision)

def addTargetToEntries(oldEntry,newEntry,tp):
    return "{:0.0{}f}".format((float(oldEntry)+float(newEntry))/2+float(tp), price_precision)

from apscheduler.schedulers.background import BackgroundScheduler
@csrf_exempt
def testing(request):
    entries=Entries.objects.all().first()
    #Calculte QTY
    info = client.futures_get_order(symbol=symbol,clientOrderId=entries.clientOrderId2,orderId=entries.orderId2)
    print(info)
    return JsonResponse({"hello":"hhh"},safe=False)
