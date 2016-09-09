#!/bin/bash
while true; do
  sudo killall openconnect
  echo "xxxx" | sudo openconnect -v --juniper <HOST> -u sbathe --passwd-on-stdin & 
  PID=$!
  echo $PID
  sleep 19m
done
