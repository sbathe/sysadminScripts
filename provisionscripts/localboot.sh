#!/bin/bash
#HOSTNAME=$1
MAC=$1
#IP=$2

# Create a DHCP entry
#echo "Creating DHCP entry....."
#echo "host $HOSTNAME {\n\t hardware ethernet  $MAC ;\n\t fixed-address $IP ;\n\t next-server 10.87.2.51 ;\n\t filename \"/var/lib/tftpboot/pxelinux.0\";\n\t option host-name \"$HOSTNAME\";\n}" | sudo tee -a /tmp/dhcpconf

# Create a PXE config
# Get the file name
echo "Creating PXE config...."
macfile=$(echo $MAC | awk -F":" '{ print "01-"$1"-"$2"-"$3"-"$4"-"$5"-"$6}')
sed -i s/default\ autoinstall/default\ hd/g /var/lib/tftpboot/pxelinux.cfg/${macfile}

#Do DNS entries:
# Not required. 

# Reload DNS and DHCP
#sudo service dhcp3-server restart

echo "Server side configuration done. Your MAC is: $MAC. You will need this for the virt server config"
