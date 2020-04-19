#!/usr/bin/python3

from sys import argv

with open('/sys/class/backlight/intel_backlight/brightness', 'r') as f:
  brightness = int(f.read().strip())

with open('/sys/class/backlight/intel_backlight/max_brightness') as f:
  max_brightness = int(f.read().strip())


if argv[1] == "up":
  brightness += 250
elif argv[1] == "down":
  brightness -= 250

if brightness > max_brightness:
  brightness = max_brightness
elif brightness < 0:
  brightness = 0

with open('/sys/class/backlight/intel_backlight/brightness', 'w') as f:
  f.write(str(brightness))
