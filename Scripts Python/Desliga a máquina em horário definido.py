#Desliga a máquina em horário definido
#Testando: 12:43
import os
import datetime
import time

hr = datetime.datetime.now()
while hr.hour != 23 or hr.minute < 50
    hr = datetime.datetime.now()

os.system("shutdown -s")
