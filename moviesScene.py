#!/usr/bin/python

from phue import Bridge

class SimpleHueSwitch:
  bridge = Bridge('192.168.0.13')
  bridge.connect()
  lights = bridge.get_light_objects('id')

  def lightsOn(self):
    if self.lights[1].on == True:
      return True
    if self.lights[2].on == True:
      return True
    if self.lights[3].on == True:
      return True
    if self.lights[5].on == True:
      return True

    return False

  def __init__(self):
    self.bridge.connect()

    if self.lightsOn() == True:
      self.bridge.set_light([1,2,3,5], 'on', False)
      print('OFF')
    else:
      self.bridge.set_light([3,5], 'on', True)
      self.bridge.set_light([3,5], 'bri', 50)

      print('ON')

switch = SimpleHueSwitch()
