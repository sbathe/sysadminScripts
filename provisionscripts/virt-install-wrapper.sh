#!/bin/bash
# Requires:
#   - Hostname
#   - MAC
sudo virt-install --connect qemu:///system \
-r 1024 -n $1 \
--vcpus 2 --pxe \
--vnc --video=cirrus --noautoconsole --hvm \
--os-type="linux" --os-variant="generic26" \
--disk pool=default,size=30 \
--network bridge=br0,mac=$2 
