#!/usr/bin/python3
import random
import prometheus_client as prom
import time
import os
#importa os modulos

status_conta_spo1 = prom.Gauge('status_do_hostspo1' , 'Status do host SPO1')
status_conta_spo2 = prom.Gauge('status_do_hostspo2' , 'Status do host SPO2')
status_conta_spo3 = prom.Gauge('status_do_hostspo3' , 'Status do host Spo3')
status_conta_21 = prom.Gauge('status_do_host21' , 'Status do host 21')
status_conta_19 = prom.Gauge('status_do_host19' , 'Status do host 19')
status_conta_51 = prom.Gauge('status_do_host51' , 'Status do host 51')
status_conta_81 = prom.Gauge('status_do_host81' , 'Status do host 81')
status_conta_85 = prom.Gauge('status_do_host85' , 'Status do host 85')


#funcoes

def getstatusspo1():
    response = os.system("ping -c 3 -W 4 10.50.11.7 > /dev/null 2>&1")
    if response == 0:
        return True
    else:
        return False

def getstatusspo2():
    response = os.system("ping -c 3 -W 4 10.50.21.7 > /dev/null 2>&1")
    if response == 0:
        return True
    else:
        return False

def getstatusspo3():
    response = os.system("ping -c 3 -W 4 10.50.31.7 > /dev/null 2>&1")
    if response == 0:
        return True
    else:
        return False

def getstatus21():
    response = os.system("nmap -sS -Pn 10.12.10.7 -p5060 > /dev/null 2>&1")
    if response == 0:
        return True
    else:
        return False

def getstatus19():
    response = os.system("nmap -sS -Pn 10.13.10.7 -p5060 > /dev/null 2>&1")
    if response == 0:
        return True
    else:
        return False

def getstatus51():
    response = os.system("nmap -sS -Pn 10.13.20.7 -p5060 > /dev/null 2>&1")
    if response == 0:
        return True
    else:
        return False

def getstatus81():
    response = os.system("nmap -sS -Pn 10.13.30.7 -p5060 > /dev/null 2>&1")
    if response == 0:
        return True
    else:
        return False

def getstatus85():
    response = os.system("nmap -sS -Pn 10.13.40.7 -p5060 > /dev/null 2>&1")
    if response == 0:
        return True
    else:
        return False

#starta o servidor http na porta 3735
if __name__ == '__main__':
   prom.start_http_server(3735)

   while True:
      try:
#            exemplo_de_cabecalho.set(getRandomNumber()*2)
            status_conta_spo1.set(getstatusspo1())
            status_conta_spo2.set(getstatusspo2())
            status_conta_spo3.set(getstatusspo3())
            status_conta_21.set(getstatus21())
            status_conta_19.set(getstatus19())
            status_conta_51.set(getstatus51())
            status_conta_81.set(getstatus81())
            status_conta_85.set(getstatus85())

      except:
         raise Exception #pass         
#aguarda 10 segundos pra executar de novo
      time.sleep(10)

