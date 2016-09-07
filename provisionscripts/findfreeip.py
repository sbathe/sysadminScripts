#!/usr/bin/python
# dhcpd_leases_parser.py
# Copyright 2008, Paul McGuire
# Sample parser to parse a dhcpd.leases file to extract leases 
# and lease attributes
# format ref: http://www.linuxmanpages.com/man5/dhcpd.leases.5.php
import sys
from pyparsing import *
import datetime,time
import subprocess
try:
  f = open("/var/lib/dhcp3/dhcpd.leases",'r')
except:
  print "Leases file /var/lib/dhcp3/dhcpd.leases no found or not readable"
  sys.exit(255)
leases = f.read()
f.close()
try:
  f = open("/etc/dhcp3/dhcpd.conf",'r')
except:
  print "Conf file /etc/dhcp3/dhcp.conf not found or not readable"
  sys.exit(255)
dcconf = f.read()
f.close()
#### Define some base constructs ####
LBRACE,RBRACE,SEMI,QUOTE,DASH = map(Suppress,'{};"-')
ipAddress = Combine(Word(nums) + ('.' + Word(nums))*3)
hexint = Word(hexnums,exact=2)
macAddress = Combine(hexint + (':'+hexint)*5)
hdwType = Word(alphanums)
yyyymmdd = Combine((Word(nums,exact=4)|Word(nums,exact=2))+
                    ('/'+Word(nums,exact=2))*2)
hhmmss = Combine(Word(nums,exact=2)+(':'+Word(nums,exact=2))*2)
dateRef = oneOf(list("0123456"))("weekday") + yyyymmdd("date") + \
                                                        hhmmss("time")
######################################
def utcToLocalTime(tokens):
    utctime = datetime.datetime.strptime("%(date)s %(time)s" % tokens,
                                                    "%Y/%m/%d %H:%M:%S")
    localtime = utctime-datetime.timedelta(0,time.timezone,0)
    tokens["utcdate"],tokens["utctime"] = tokens["date"],tokens["time"]
    tokens["localdate"],tokens["localtime"] = str(localtime).split()
    del tokens["date"]
    del tokens["time"]
dateRef.setParseAction(utcToLocalTime)
### Statements for lease file ###
startsStmt = "starts" + dateRef + SEMI
endsStmt = "ends" + (dateRef | "never") + SEMI
tstpStmt = "tstp" + dateRef + SEMI
clttStmt = "cltt" + dateRef + SEMI
hdwStmt = "hardware" + hdwType("type") + macAddress("mac") + SEMI
uidStmt = "uid" + QuotedString('"')("uid") + SEMI
bindingStmt = "binding" + Word(alphanums) + Word(alphanums) + SEMI
nextbindingStmt = "next binding" + Word(alphanums) + Word(alphanums) + SEMI
hostnameStmt = "client-hostname" + QuotedString('"') + SEMI

leaseStatement = startsStmt | endsStmt | tstpStmt | clttStmt | hdwStmt | \
                                   uidStmt | bindingStmt | nextbindingStmt | hostnameStmt
leaseDef = "lease" + ipAddress("ipaddress") + LBRACE + \
                            Dict(ZeroOrMore(Group(leaseStatement))) + RBRACE
###################################
fixaddStmt = "fixed" + DASH + Word(alphanums) + ipAddress("ipaddress") + SEMI
dchostnameStmt = "option host-name" + QuotedString('"') + SEMI
filenameStmt = "filename" + QuotedString('"') + SEMI
servernameStmt = "server-name" + QuotedString('"') + SEMI
nextserverStmt = "next-server" + ipAddress + SEMI
hostname = Word(printables) 
#hostnameExt = Word(alphanums) + ZeroOrMore("-" + hostname)

dcStmt = fixaddStmt | dchostnameStmt | filenameStmt | servernameStmt | hdwStmt | nextserverStmt
dcDef  = "host" + hostname("hostname") + LBRACE + \
                           Dict(ZeroOrMore(Group(dcStmt))) + RBRACE
### Get ipaddress/mac pair from leases
ipmacinfo = {}
ipaddresses = []
for lease in leaseDef.searchString(leases):
#  print lease.ipaddress,';',lease.hardware.mac
  ipmacinfo[lease.hardware.mac] = { lease.ipaddress: "" }
  ipaddresses.append(lease.ipaddress)
### Get ipaddress/mac pair from dhcpdconf
for dcdef in dcDef.searchString(dcconf):
#  print dcdef.hostname,';',dcdef.fixed.ipaddress,';',dcdef.hardware.mac
  ipmacinfo[dcdef.hardware.mac] = { dcdef.fixed.ipaddress: dcdef.hostname }
  ipaddresses.append(dcdef.fixed.ipaddress)

args = ['fping', '-u', '-r', '1', '-g', '10.87.1.1', '10.87.1.200']
p = subprocess.Popen(args,stderr=subprocess.PIPE,stdout=subprocess.PIPE)
freeips = p.communicate()[0].split("\n")

for count in range(len(freeips)):
  freeip = freeips.pop(count)
  if freeip in ipaddresses:
    pass
  else:
    print freeip
    break


