#!/usr/bin/python3
import prometheus_client as prom
import subprocess
import time
import re
#importa os modulos

###  Agrupamento de PIPES [INÍCIO]  ###

def getDetalhamento():
   command = "fs_cli -x 'sofia status'"
   result = str(subprocess.check_output(command, shell=True))
   return result

def filtrarResumo(entrada: str):
    linhas = entrada.replace("\\n", "\n")
    linhas = entrada.split('\n')

    resumo = []
    for linha in linhas:
        if 'profile' not in linha.split(' '):
            continue

        # pipe = buscarContaSip(linha)
        # if(pipe == None):
        #     continue
        pipe = buscarPrimeiroElementoValidoLista(linha.split(' '))
        qnt = extrairNumero(getUltimoElementoLista(linha.split(' ')))
        resumo.append({'pipe': pipe, 'count': qnt})
    return resumo

def buscarPrimeiroElementoValidoLista(arr: list):
    valor = ''
    for pedaco in arr:
        if pedaco != "":
            valor = pedaco
            break
    return valor

def buscarContaSip(linha: str):
    valor = re.search('sip:(.*)@', linha)
    if(valor != None):
        return valor.group(1)
    return valor

def extrairNumero(string: str):
    valor = re.sub('\D', '', string)
    if valor != "":
        valor = int(valor)
    else:
        valor = 0
    return valor

def getUltimoElementoLista(arr: list): 
    if len(arr) > 0:
        return arr[len(arr) - 1]
    return None

def checarSeVariavelExiste(string: str):
    if string in locals():
        return True
    return False

def setarValorGauge(variavel: str, valor: int):
    if not checarSeVariavelExiste(variavel):
        exec(variavel + " = prom.Gauge('freeswitch_channels_" + variavel + "','Freeswitch active channels count')")
    exec(variavel + ".set(" + valor + " * 2)")
    return True
    
###  Agrupamento de PIPES [FIM]  ###

#============================HTTP===============================

#starta o servidor http na porta 3733
if __name__ == '__main__':
   prom.start_http_server(3734)

   while True:
      try:

         # Gerar dinamicamente os gráficos de agrupamento
         items = filtrarResumo(getDetalhamento)
         for item in items:
            setarValorGauge(item['pipe'], item['valor'])

      except:
         raise Exception #pass         
#aguarda 5 segundos pra executar de novo
      time.sleep(5)
