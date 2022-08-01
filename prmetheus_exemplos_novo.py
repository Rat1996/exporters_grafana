#!/usr/bin/python3
import random
import prometheus_client as prom
import subprocess
import time
import re
#importa os modulos

#============================headers===============================

#gera o formato da metrica no prometheus
#exemplo_de_cabecalho = prom.Gauge('contador1' , 'Exemplo de titulo')

#ebt_spo1_5061 = prom.Gauge('freeswitch_channels_active_spo1','Freeswitch active channels count')
#ebt_spo2_5062 = prom.Gauge('freeswitch_channels_active_spo2','Freeswitch active channels count')
#ebt_spo3_5063 = prom.Gauge('freeswitch_channels_active_spo3','Freeswitch active channels count')
#open_english = prom.Gauge('freeswitch_channels_active_open_english','Freeswitch active channels count')
#hiya_reput_spo1 = prom.Gauge('freeswitch_channels_active_hiya_reput_spo1','Freeswitch active channels count')
#sp_tdm11 = prom.Gauge('freeswitch_channels_active_sp_tdm11','Freeswitch active channels count')
#sp_tdm21 = prom.Gauge('freeswitch_channels_active_sp_tdm21','Freeswitch active channels count')
#ebt_cnl21 = prom.Gauge('freeswitch_channels_active_ebt_cnl21','Freeswitch active channels count')

#============================Functions===============================


#funcao que executa o numero aleatorio num range de 5 a 1000 de 5 em 5
#def getRandomNumber():
#	numero_random = random.randrange(5,1000,5)
#	return numero_random



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

#enquanto verdadeiro, imprime a metrica chamando a funcao getrandomnumber
#neste caso sempre vai ser verdadeiro, pra que possa sempre imprimir de novo
   while True:
      try:
         #exemplo_de_cabecalho.set(getRandomNumber()*2)


         # Gerar dinamicamente os gráficos de agrupamento
         items = filtrarResumo(getDetalhamento)
         for item in items:
            setarValorGauge(item['pipe'], item['valor'])

      except:
         raise Exception #pass         
#aguarda 5 segundos pra executar de novo
      time.sleep(5)