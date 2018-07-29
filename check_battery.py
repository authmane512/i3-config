#!/usr/bin/python3

import os
import time
import sys

while True:
  charge = int(os.popen("acpi").read().split(", ")[1].rstrip("%"))
  with open("/tmp/check_battery.log", "a") as f:
    f.write("{}: current charge of {}%\n".format(time.ctime(), charge))
  if charge <= int(sys.argv[1]):
    os.system('i3-nagbar -t warning -m "Warning: battery is low!"')
  time.sleep(10)
