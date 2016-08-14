#!/usr/bin/python
from phue import Bridge
import random

b = Bridge('192.168.0.13')

#If running for the first time, press button on bridge and run with b.connect() uncommented
#b.connect()
#for light in ['Kitchen', 'Bedroom', 'Garage']
#    light_names[light].on = True
#    light_names[light].hue = 15000
#    light_names[light].saturation = 120

#lights = b.lights
#b.set_light([1,2,3,5], 'on', False)
lights_list = b.get_light_objects('list')
lights = b.get_light_objects('id')

def lightsOn():
    if self.lights[1].on == False:
      if lights[2].on == False:
        if lights[3].on == False:
         if lights[5].on == False:
          return True

    return False

lightsOn = lightsOn()

if lights[1].on == True:
  print('1 on')
  b.set_light([1,2,3,5], 'on', False)
elif lights[2].on == True:
  print('2 on')
  b.set_light([1,2,3,5], 'on', False)
elif lights[3].on == True:
  print('3 on')
  b.set_light([1,2,3,5], 'on', False)
elif lights[5].on == True:
  print('5 on')
  b.set_light([1,2,3,5], 'on', False)
