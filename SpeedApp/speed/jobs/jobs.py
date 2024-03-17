from binance.client import Client
import requests
import logging
import time
import math

logger=logging.getLogger("jobs")

# key="5AciUnbYRHOp3jqFPQDUCqjzrM4Gt6iY9Rk1lK4XbPrDguCDh5FzQCZZd7aEsX1p"
# secret="1RBXR8IdgU9Vrk0EGUHL5ELfXAydjUDM9csQH1btme9SLxfl8LpLdaShWYoJ2RE6"
# client = Client(api_key=key,api_secret=secret)
symbol="CHRUSDT"
def job_1():
    


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
                    "txt":[
                        {
                            "distance":distance,
                            "New Entry":support1,
                            "New Entry 2":support2,
                            "New Entry 3":support3,
                            "New Entry 4":support4,
                        }
                    ]
                }
                requests.get("http://127.0.0.1:8000/bot/firstbot",params=SignalParams)
    except Exception as e:
        logger.error(e)