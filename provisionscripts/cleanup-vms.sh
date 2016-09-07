#!/bin/bash
echo "Cleaning up $1...."
echo "Destroying the VM if it is running..."
sudo virsh destroy $1
echo "Removing the backing image..."
sudo rm /var/lib/libvirt/images/${1}.img 
echo "Removing libvirt config..."
sudo rm /etc/libvirt/qemu/${1}.xml 
virsh undefine $1
