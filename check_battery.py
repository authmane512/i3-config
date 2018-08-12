#!/usr/bin/python3

import os
import time
import sys

while True:
  charge = int(os.popen("acpi").read().split(", ")[1].rstrip("%\n"))
  status = os.popen("acpi").read().split(", ")[0].split()[-1]
  print(charge, status)

  if charge <= int(sys.argv[1]) and status == "Discharging":
    os.system('i3-nagbar -t warning -m "Warning: battery is low!"')
  elif charge == 100 and status != "Discharging":
    os.system('i3-nagbar -t warning -m "Warning: battery is full!"')

  time.sleep(60)
