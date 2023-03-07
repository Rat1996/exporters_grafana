#!/usr/local/bin/python3
import subprocess
import prometheus_client as prom
import time
import os
#importa os modulos

opensips_load = prom.Gauge('opensips_load' , 'Load do servico OpenSips')

#funcoes
def getopensipsload():
   comando = os.popen("/sbin/opensipsctl fifo get_statistics load: | awk '{print $2}'").read()
   resultado = int(comando)
   return resultado

#starta o servidor http na porta 3740
if __name__ == '__main__':
   prom.start_http_server(3740)

   while True:
      try:
            opensips_load.set(getopensipsload())
      except:
         raise Exception #pass         
#aguarda 10 segundos pra executar de novo
      time.sleep(4)