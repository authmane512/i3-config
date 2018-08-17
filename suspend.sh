#!/bin/bash

if [ "$(vboxmanage list runningvms)" = "" ]; then
  i3lock -i .lockscreen.png
  sleep 1
  sudo pm-suspend
else
  i3-nagbar -m "Error: You forgot to suspend a VirtualBox VM!" -t error
fi
