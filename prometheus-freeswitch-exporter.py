#!/usr/bin/python3
import subprocess
import prometheus_client as prom
import time

active_calls = prom.Gauge('freeswitch_calls_active',
                          'Freeswitch active calls count')
ringing_calls = prom.Gauge('freeswitch_calls_ringing',
                           'Freeswitch ringing calls count')
early_media_calls = prom.Gauge(
    'freeswitch_calls_early', 'Freeswitch early media calls count')
down_calls = prom.Gauge('freeswitch_calls_down', 'Freeswitch down calls count')

all_calls = prom.Gauge('freeswitch_calls_all','Freeswitch all calls count')

active_channels = prom.Gauge(
    'freeswitch_channels_active', 'Freeswitch active channels count')


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

      except:
         raise Exception #pass         

      time.sleep(5)