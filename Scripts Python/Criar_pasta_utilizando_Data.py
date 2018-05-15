#Scripts Python - Amaury
import datetime
import time
import os
today=time.strftime('%Y%m%d')
hour=time.strftime('%h')
if(hour<12): h = "00"
else: h ="12"
os.system("mkdir /home/xxx/"+str(today)+""+str(h)+"")