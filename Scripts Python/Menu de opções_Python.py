import os
import platform
import locale
print(locale)
so = platform.system()
print ("Seu Sistema Operacional e {}".format(so))
host = input("Digite seu Endereco de Host ")
pacote = int(input("Quantos Pacotes deseja ser enviado?"))
resposta = os.system("ping -c" + str(pacote) + " " + host)
if resposta ==0:
    print(host, 'Online')
else:
    resposta = os.system("traceroute " + host)
