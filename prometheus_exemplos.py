#!/usr/bin/python3
import subprocess
import prometheus_client as prom
import time

active_calls = prom.Gauge('freeswitch_calls_active', 'Freeswitch active calls count')
ringing_calls = prom.Gauge('freeswitch_calls_ringing', 'Freeswitch ringing calls count')
early_media_calls = prom.Gauge('freeswitch_calls_early', 'Freeswitch early media calls count')
down_calls = prom.Gauge('freeswitch_calls_down', 'Freeswitch down calls count')
all_calls = prom.Gauge('freeswitch_calls_all','Freeswitch all calls count')
active_channels = prom.Gauge('freeswitch_channels_active', 'Freeswitch active channels count')

active_calls_TDM11 = prom.Gauge('freeswitch_calls_active_TDM11', 'Freeswitch active calls count')
active_calls_TDM13 = prom.Gauge('freeswitch_calls_active_TDM13', 'Freeswitch active calls count')
active_calls_TDM15 = prom.Gauge('freeswitch_calls_active_TDM15', 'Freeswitch active calls count')
active_calls_TDM17 = prom.Gauge('freeswitch_calls_active_TDM17', 'Freeswitch active calls count')
active_calls_TDM21 = prom.Gauge('freeswitch_calls_active_TDM21', 'Freeswitch active calls count')
active_calls_TDM22 = prom.Gauge('freeswitch_calls_active_TDM22', 'Freeswitch active calls count')
active_calls_TDM34 = prom.Gauge('freeswitch_calls_active_TDM34', 'Freeswitch active calls count')
active_calls_TDM35 = prom.Gauge('freeswitch_calls_active_TDM35', 'Freeswitch active calls count')
active_calls_TDM37 = prom.Gauge('freeswitch_calls_active_TDM37', 'Freeswitch active calls count')
active_calls_TDM47 = prom.Gauge('freeswitch_calls_active_TDM47', 'Freeswitch active calls count')
active_calls_TDM61 = prom.Gauge('freeswitch_calls_active_TDM61', 'Freeswitch active calls count')
active_calls_TDM67 = prom.Gauge('freeswitch_calls_active_TDM67', 'Freeswitch active calls count')
active_calls_TDM82 = prom.Gauge('freeswitch_calls_active_TDM82', 'Freeswitch active calls count')
active_calls_TDM84 = prom.Gauge('freeswitch_calls_active_TDM84', 'Freeswitch active calls count')
active_calls_TDM88 = prom.Gauge('freeswitch_calls_active_TDM88', 'Freeswitch active calls count')

active_calls_CNL = prom.Gauge('freeswitch_calls_active_CNL', 'Freeswitch active calls count')

active_channels_11 = prom.Gauge('freeswitch_channels_active_11', 'Freeswitch active channels count')
active_channels_13 = prom.Gauge('freeswitch_channels_active_13', 'Freeswitch active channels count')
active_channels_15 = prom.Gauge('freeswitch_channels_active_15', 'Freeswitch active channels count')
active_channels_17 = prom.Gauge('freeswitch_channels_active_17', 'Freeswitch active channels count')
active_channels_21 = prom.Gauge('freeswitch_channels_active_21', 'Freeswitch active channels count')
active_channels_22 = prom.Gauge('freeswitch_channels_active_22', 'Freeswitch active channels count')
active_channels_34 = prom.Gauge('freeswitch_channels_active_34', 'Freeswitch active channels count')
active_channels_35 = prom.Gauge('freeswitch_channels_active_35', 'Freeswitch active channels count')
active_channels_37 = prom.Gauge('freeswitch_channels_active_37', 'Freeswitch active channels count')
active_channels_47 = prom.Gauge('freeswitch_channels_active_47', 'Freeswitch active channels count')
active_channels_61 = prom.Gauge('freeswitch_channels_active_61', 'Freeswitch active channels count')
active_channels_67 = prom.Gauge('freeswitch_channels_active_67', 'Freeswitch active channels count')
active_channels_82 = prom.Gauge('freeswitch_channels_active_82', 'Freeswitch active channels count')
active_channels_84 = prom.Gauge('freeswitch_channels_active_84', 'Freeswitch active channels count')
active_channels_88 = prom.Gauge('freeswitch_channels_active_88', 'Freeswitch active channels count')


#================/ FUNCOES /================

def clearFreeswitchCommandResult(inputString: str):
   inputString = inputString.replace("\\n", "\n")
   inputString = inputString.split('\n')
   return inputString


def getCallsByStatus(status: str, inputList: list):
   statusCount = 0
   for line in inputList[1:-4]:
      fields = line.split(',')
      if status in fields[13]:
         statusCount = statusCount + 1
   return statusCount


def getFreeswitchCallsInfo():
   freeswitch_command = 'fs_cli -x "show calls"'
   result = clearFreeswitchCommandResult(
       str(subprocess.check_output(freeswitch_command, shell=True)))
   return result


def getFreeswitchChannelsInfo():
   freeswitch_command = 'fs_cli -x "status"'
   result = clearFreeswitchCommandResult(
       str(subprocess.check_output(freeswitch_command, shell=True)))
   return result[3].split(' ')[0]

def getCallsByStatusTDM11(status: str, inputList: list):
    statusCount = 0
    for line in inputList[1:-4]:
       fields = line.split(',')
       if status in fields[13] and 'EBT_CNL11' in fields[4]:
          statusCount = statusCount + 1
    return statusCount
      
def getCallsByStatusTDM13(status: str, inputList: list):
    statusCount = 0
    for line in inputList[1:-4]:
       fields = line.split(',')
       if status in fields[13] and 'EBT_CNL13' in fields[4]:
          statusCount = statusCount + 1
    return statusCount
      
def getCallsByStatusTDM15(status: str, inputList: list):
    statusCount = 0
    for line in inputList[1:-4]:
       fields = line.split(',')
       if status in fields[13] and 'EBT_CNL15' in fields[4]:
          statusCount = statusCount + 1
    return statusCount
      
def getCallsByStatusTDM17(status: str, inputList: list):
    statusCount = 0
    for line in inputList[1:-4]:
       fields = line.split(',')
       if status in fields[13] and 'EBT_CNL17' in fields[4]:
          statusCount = statusCount + 1
    return statusCount
      
def getCallsByStatusTDM21(status: str, inputList: list):
    statusCount = 0
    for line in inputList[1:-4]:
       fields = line.split(',')
       if status in fields[13] and 'EBT_CNL21' in fields[4]:
          statusCount = statusCount + 1
    return statusCount
      
def getCallsByStatusTDM22(status: str, inputList: list):
    statusCount = 0
    for line in inputList[1:-4]:
       fields = line.split(',')
       if status in fields[13] and 'EBT_CNL22' in fields[4]:
          statusCount = statusCount + 1
    return statusCount
      
def getCallsByStatusTDM34(status: str, inputList: list):
    statusCount = 0
    for line in inputList[1:-4]:
       fields = line.split(',')
       if status in fields[13] and 'EBT_CNL34' in fields[4]:
          statusCount = statusCount + 1
    return statusCount
    
def getCallsByStatusTDM35(status: str, inputList: list):
    statusCount = 0
    for line in inputList[1:-4]:
       fields = line.split(',')
       if status in fields[13] and 'EBT_CNL35' in fields[4]:
          statusCount = statusCount + 1
    return statusCount
      
def getCallsByStatusTDM37(status: str, inputList: list):
    statusCount = 0
    for line in inputList[1:-4]:
       fields = line.split(',')
       if status in fields[13] and 'EBT_CNL37' in fields[4]:
          statusCount = statusCount + 1
    return statusCount
      
def getCallsByStatusTDM47(status: str, inputList: list):
    statusCount = 0
    for line in inputList[1:-4]:
       fields = line.split(',')
       if status in fields[13] and 'EBT_CNL47' in fields[4]:
          statusCount = statusCount + 1
    return statusCount
      
def getCallsByStatusTDM61(status: str, inputList: list):
    statusCount = 0
    for line in inputList[1:-4]:
       fields = line.split(',')
       if status in fields[13] and 'EBT_CNL61' in fields[4]:
          statusCount = statusCount + 1
    return statusCount
      
def getCallsByStatusTDM67(status: str, inputList: list):
    statusCount = 0
    for line in inputList[1:-4]:
       fields = line.split(',')
       if status in fields[13] and 'EBT_CNL67' in fields[4]:
          statusCount = statusCount + 1
    return statusCount
      
def getCallsByStatusTDM82(status: str, inputList: list):
    statusCount = 0
    for line in inputList[1:-4]:
       fields = line.split(',')
       if status in fields[13] and 'EBT_CNL82' in fields[4]:
          statusCount = statusCount + 1
    return statusCount
      
def getCallsByStatusTDM84(status: str, inputList: list):
    statusCount = 0
    for line in inputList[1:-4]:
       fields = line.split(',')
       if status in fields[13] and 'EBT_CNL84' in fields[4]:
          statusCount = statusCount + 1
    return statusCount
      
def getCallsByStatusTDM88(status: str, inputList: list):
    statusCount = 0
    for line in inputList[1:-4]:
       fields = line.split(',')
       if status in fields[13] and 'EBT_CNL88' in fields[4]:
          statusCount = statusCount + 1
    return statusCount

def getCallsByStatusCNL(status: str, inputList: list):
   statusCount = 0
   for line in inputList[1:-4]:
      fields = line.split(',')
      if status in fields[13] and 'Embratel_SPO_Movel' in fields[4]:
         statusCount = statusCount + 1
   return statusCount

def getActiveCnl(status: str, inputList: list):
   statusCount = 0
   for line in inputList[1:-4]:
      fields = line.split(',')
      if status in fields[4]:
         statusCount = statusCount + 1
   return statusCount

#================/ HTTP /================

if __name__ == '__main__':
   prom.start_http_server(3733)

   while True:

      try:
         freeSwitchCallsLog = getFreeswitchCallsInfo()
         
         active_calls.set(getCallsByStatus('ACTIVE', freeSwitchCallsLog))
         ringing_calls.set(getCallsByStatus('RINGING', freeSwitchCallsLog))
         early_media_calls.set(getCallsByStatus('EARLY', freeSwitchCallsLog))
         down_calls.set(getCallsByStatus('DOWN', freeSwitchCallsLog))
         active_channels.set(getFreeswitchChannelsInfo())
         all_calls.set(len(freeSwitchCallsLog[1:-4]))

         active_calls_CNL.set(getCallsByStatusCNL('ACTIVE', freeSwitchCallsLog))

         active_calls_TDM11.set(getCallsByStatusTDM11('ACTIVE', freeSwitchCallsLog))
         active_calls_TDM13.set(getCallsByStatusTDM13('ACTIVE', freeSwitchCallsLog))
         active_calls_TDM15.set(getCallsByStatusTDM15('ACTIVE', freeSwitchCallsLog))
         active_calls_TDM17.set(getCallsByStatusTDM17('ACTIVE', freeSwitchCallsLog))
         active_calls_TDM21.set(getCallsByStatusTDM21('ACTIVE', freeSwitchCallsLog))
         active_calls_TDM22.set(getCallsByStatusTDM22('ACTIVE', freeSwitchCallsLog))
         active_calls_TDM34.set(getCallsByStatusTDM34('ACTIVE', freeSwitchCallsLog))
         active_calls_TDM35.set(getCallsByStatusTDM35('ACTIVE', freeSwitchCallsLog))
         active_calls_TDM37.set(getCallsByStatusTDM37('ACTIVE', freeSwitchCallsLog))
         active_calls_TDM47.set(getCallsByStatusTDM47('ACTIVE', freeSwitchCallsLog))
         active_calls_TDM61.set(getCallsByStatusTDM61('ACTIVE', freeSwitchCallsLog))
         active_calls_TDM67.set(getCallsByStatusTDM67('ACTIVE', freeSwitchCallsLog))
         active_calls_TDM82.set(getCallsByStatusTDM82('ACTIVE', freeSwitchCallsLog))
         active_calls_TDM84.set(getCallsByStatusTDM84('ACTIVE', freeSwitchCallsLog))
         active_calls_TDM88.set(getCallsByStatusTDM88('ACTIVE', freeSwitchCallsLog))

         active_channels_11.set(getActiveCnl('EBT_CNL11', freeSwitchCallsLog)*2)
         active_channels_13.set(getActiveCnl('EBT_CNL13', freeSwitchCallsLog)*2)
         active_channels_15.set(getActiveCnl('EBT_CNL15', freeSwitchCallsLog)*2)
         active_channels_17.set(getActiveCnl('EBT_CNL17', freeSwitchCallsLog)*2)
         active_channels_21.set(getActiveCnl('EBT_CNL21', freeSwitchCallsLog)*2)
         active_channels_22.set(getActiveCnl('EBT_CNL22', freeSwitchCallsLog)*2)
         active_channels_34.set(getActiveCnl('EBT_CNL34', freeSwitchCallsLog)*2)
         active_channels_35.set(getActiveCnl('EBT_CNL35', freeSwitchCallsLog)*2)
         active_channels_37.set(getActiveCnl('EBT_CNL37', freeSwitchCallsLog)*2)
         active_channels_47.set(getActiveCnl('EBT_CNL47', freeSwitchCallsLog)*2)
         active_channels_61.set(getActiveCnl('EBT_CNL61', freeSwitchCallsLog)*2)
         active_channels_67.set(getActiveCnl('EBT_CNL67', freeSwitchCallsLog)*2)
         active_channels_82.set(getActiveCnl('EBT_CNL82', freeSwitchCallsLog)*2)
         active_channels_84.set(getActiveCnl('EBT_CNL84', freeSwitchCallsLog)*2)
         active_channels_88.set(getActiveCnl('EBT_CNL88', freeSwitchCallsLog)*2)
         
      except:
         raise Exception #pass         

      time.sleep(5)


