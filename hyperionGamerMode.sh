#!/bin/sh
SERVICE=hyperion
if systemctl is-active $SERVICE >/dev/null 2>&1
then
  echo "Stop Hyperion"
  sudo hyperion-remote --priority 50 --color blue
else
  echo "Start Hyperion"
  sudo systemctl start $SERVICE
  sleep 3
  sudo hyperion-remote --priority 50 --color blue
fi
