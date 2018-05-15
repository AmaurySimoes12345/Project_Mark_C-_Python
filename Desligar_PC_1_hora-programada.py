#Scripts Python - Amaury
import time
import sys
import os

time_to_shutdown=sys.argv[1]
hours=time_to_shutdown.split(':')[0]
min=time_to_shutdown.split(':')[1]
text="""print("SAI JA' DO PC E VAI ESTUDAR!")
print("VE LA' SE NAO QUERES LEVAR COM O PAU!")
raw_input('<enter> para fechar do aviso')"""

x=0
while True:
    actual_hours=time.strftime("%H")
    actual_min=time.strftime("%M")
    if x==0 and int(actual_hours)==int(hours) and int(min)-int(actual_min)==5:
        file("warn.py",'w').write(text)
        os.system("warn.py")
        os.remove("warn.py")
        x=1
    elif x==1 and int(actual_hours)==int(hours) and int(min)==int(actual_min): break

os.system("shutdown -s")