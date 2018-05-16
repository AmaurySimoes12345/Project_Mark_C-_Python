#Scripts Python - Amaury
import os.path
import sys
import tempfile
import datetime
import time

today=time.strftime('%Y%m%d')
hour=time.strftime('%h')
if(hour<12): h = "00"
else: h ="12"
os.system("mkdir /home/xxx/"+str(today)+""+str(h)+"")