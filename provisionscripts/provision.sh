#!/bin/bash
#HOSTNAME=$1
MAC=$(/home/vmadmin/bin/generatemac.sh)
echo "Finding free IP. This might take a few seconds"
IP=$(/home/vmadmin/bin/findfreeip.py)
a=$(echo $IP | cut -d"." -f4)
b=$((a-50))
HOSTNAME=bjninqa${b} 
 
# Create a DHCP entry
echo "Creating DHCP entry....."
echo -e "host $HOSTNAME {\n\t hardware ethernet  $MAC ;\n\t fixed-address $IP ;\n\t next-server 10.87.2.51 ;\n\t filename \"/var/lib/tftpboot/pxelinux.0\";\n\t option host-name \"$HOSTNAME\";\n}" | tee -a /tmp/dhcpconf

# Create a PXE config
# Get the file name
echo "Creating PXE config...."
macfile=$(echo $MAC | awk -F":" '{ print "01-"$1"-"$2"-"$3"-"$4"-"$5"-"$6}')
echo -e "DISPLAY ubuntu-installer/amd64/boot-screens/boot.txt\ndefault autoinstall\nLABEL autoinstall\nkernel ubuntu-installer/amd64/linux\nappend ramdisk_size=14984 locale=en_US console-setup/layoutcode=us netcfg/choose_interface=eth0 netcfg/get_hostname=denimserver netcfg/get_domain=bluejeansnet.com url=http://10.87.2.51/preseed-kvm.cfg vga=normal initrd=ubuntu-installer/amd64/initrd.gz --\nprompt 0\ntimeout 5\nlabel hd\nlocalboot 0x80" | tee /var/lib/tftpboot/pxelinux.cfg/${macfile}

#Do DNS entries:
# Not required. 
#RET=$(grep -w $HOSTNAME /etc/bind/zones/db.in.bluejeansnet.com)
#if [ $RET == 1 ]; then
#  echo "Creating DNS entry..."
#  echo -e "$HOSTNAME              IN      A               $IP\n"
#  date=$(date +%Y%m%d)
#  serial=$(grep -i serial /etc/bind/zones/db.in.bluejeansnet.com | gawk '{print $1}')
#  sed -i -e 's#[[:digit:]].*serial#$date\ \;\ serial#' 
# Reload DNS and DHCP
#sudo service dhcp3-server restart
echo "Restarting the DHCP server...." 
sudo /etc/init.d/dhcp3-server restart
echo "Server side configuration done. Your MAC is: $MAC You will need this for the virt server config. And the IP is: $IP"
