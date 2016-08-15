#!/usr/bin/python

import json
from phue import Bridge

class SimpleHueSwitch:  

  def getConfigs(self):
    with open('/home/osmc/myHueLights/config.json') as data_file:    
      data = json.load(data_file)
    return data

  def lightsOn(self, lights):
    if lights[4].on == True:
      return True
    if lights[6].on == True:
      return True

    return False

  def __init__(self):
    config = self.getConfigs()
    ip_bridge = config["ip_bridge"]
   
    bridge = Bridge(ip_bridge)
    bridge.connect()
    lights = bridge.get_light_objects('id')
    
    if self.lightsOn(lights) == True:
       bridge.set_light([4,6], 'on', False)
       print('OFF')
    else:
       bridge.set_light([4,6], 'on', True)
       bridge.set_light([4,6], 'xy', [0.3227,0.329])
       bridge.set_light([4,6], 'bri', 160)
       print('ON')

switch = SimpleHueSwitch()
