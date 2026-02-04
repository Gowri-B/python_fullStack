#date,time,math,random,os

import datetime
import time

while True:
    now=datetime.datetime.now()
    Current_time = now.strftime("%H:%M:%S")

    #print(Current_time)
    print(f"\r {Current_time}",end = "",flush=True)

    '''
        \r-carriage return 
        end=""
        flush=True
    '''

    time.sleep(1)