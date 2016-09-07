#!/bin/sh
INTERNAL_NETWORK=\"192.168.1.0/24\"
ROUTER_IP=\"192.168.1.1\"
PROXY_SERVER=\"192.168.1.113\"
PROXY_PORT=\"3128\"
if [ -z $TRANSPARENT_PROXY ]; then
  /usr/sbin/iptables -t nat -D PREROUTING -i br0 -s $INTERNAL_NETWORK -d $INTERNAL_NETWORK -p tcp --dport 80 -j ACCEPT
  /usr/sbin/iptables -t nat -D PREROUTING -i br0 -s ! $PROXY_SERVER -p tcp --dport 80 -j DNAT --to $PROXY_SERVER:$PROXY_PORT
  /usr/sbin/iptables -t nat -D POSTROUTING -o br0 -s $INTERNAL_NETWORK -p tcp -d $PROXY_SERVER -j SNAT --to $ROUTER_IP
  /usr/sbin/iptables -t filter -D FORWARD -s $INTERNAL_NETWORK -d $PROXY_SERVER -i br0 -o br0 -p tcp --dport $PROXY_PORT -j ACCEPT
  export TRANSPARENT_PROXY=\"1\"
else
  echo \"This script has already run!\"
  echo \"If it hasn\'t, unset \$TRANSPARENT_PROXY manually via the shell.\"
fi
