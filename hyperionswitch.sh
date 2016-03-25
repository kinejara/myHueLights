#!/bin/sh
SERVICE=hyperion
if systemctl is-active $SERVICE >/dev/null 2>&1
then
  echo "Stop Hyperion"
  sudo hyperion-remote --priority 50 --color blue --duration 1000
  sudo hyperion-remote --priority 50 --color black --duration 5000
  sudo systemctl stop $SERVICE
  [ -f /storage/.cache/services/$SERVICE.conf ] && mv /storage/.cache/services/$SERVICE.conf /storage/.cache/services/$SERVICE.disabled
  /usr/bin/xbmc-send --host=127.0.0.1 --port=9778 --action="Notification(Hyperion,Shutting Down)"
else
  echo "Start Hyperion"
  [ -f /storage/.cache/services/$SERVICE.disabled ] && mv /storage/.cache/services/$SERVICE.disabled /storage/.cache/services/$SERVICE.conf
  [ ! -f /storage/.cache/services/$SERVICE.conf ] && touch /storage/.cache/services/$SERVICE.conf
  sudo systemctl start $SERVICE
  /usr/bin/xbmc-send --host=127.0.0.1 --port=9778 --action="Notification(Hyperion,Starting Up)"
fi
