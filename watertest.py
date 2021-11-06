import datetime
import RPi.GPIO as GPIO 
import time 
from relayhandler import controlrelay 
GPIOPin= 7 
controlrelay(GPIOPin,0)
while True:
    now = datetime.datetime.now()  
    day=int(time.strftime("%w"))  
    if (day==1 or day==3 or day ==5 ): 
        if now.hour == 9 and now.minute == 45 and now.second < 4 :  
          controlrelay(GPIOPin,1)
        else: 
          controlrelay(GPIOPin,0)
    time.sleep(0.3)







