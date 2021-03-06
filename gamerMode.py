#!/usr/bin/python

import json
import subprocess
from phue import Bridge

class SimpleHueSwitch:
  
  def getConfigs(self):
    with open('/home/osmc/myHueLights/config.json') as data_file:    
      data = json.load(data_file)
    return data
  
  def lightsOn(self, lights):
    if lights[1].on == True:
      return True
    if lights[2].on == True:
      return True
    if lights[3].on == True:
      return True
    if lights[5].on == True:
      return True

    return False

  def __init__(self):
    config = self.getConfigs()
    ip_bridge = config["ip_bridge"]
    hyperionPath = config["hyperionPath"]
   
    bridge = Bridge(ip_bridge)
    bridge.connect()
    lights = bridge.get_light_objects('id')

    if self.lightsOn(lights) == True:
      bridge.set_light([1,2,3,5], 'on', False)
      print('OFF')
    else:
      bridge.set_light([1,2,3,5], 'on', True)
      bridge.set_light([1,2,3,5], 'xy', [0.139,0.081])
      bridge.set_light([1,2], 'bri', 5)
      bridge.set_light([3,5], 'bri', 100)
      subprocess.call(hyperionPath, shell=True)

      print('ON')

switch = SimpleHueSwitch()
