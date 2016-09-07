#!/usr/bin/python
# [timestamp] SERVICE ALERT:         host_name;service_description;service_state,servicestate_type,service_check_attempt;plugin_output
# [timestamp] CURRENT SERVICE STATE: host_name;service_description;service_state,servicestate_type,service_check_attempt;plugin_output

# [timestamp] HOST ALERT: host_name;hoststate;hoststatetype;hostattempt;plugin_output
# [timestamp] CURRENT HOST STATE: host_name;hoststate;hoststatetype;hostattempt;plugin_output
# [1469571413] SERVICE NOTIFICATION: stage-alerts;sj1-stage-a2-102-22;check_all_disks-0;WARNING;service-mail-notification-cmd;DISK WARNING - free space: / 5215 MB (8% inode=74%): /dev 8013 MB (99% inode=99%): /run 1604 MB (99% inode=99%): /run/lock 5 MB (100% inode=99%): /run/shm 8024 MB (100% inode=99%):;
# [timestamp] SERVICE NOTIFICATION: notification_group;host_name;service_description;service_state;notification_cmd;plugin_output
''' Flow:
    TRACK: 
    - Soft state changes, 
    - Hard state changes. 
    We need top chatters for
    - unique hard state changes
    - unique soft state changes
    - notifications sent
  1. Read a line
  2. If it is a Current state line, just note and update current and last states
    - If there is no last_state, make current state the last state
  3. For ALERT lines, if a service changes from OK to any of the other states, we have a unique alert
    - If the state type is SOFT, dont update the last_state, else update last_state
    - else, just update notification count

'''

import yaml
import re
from collections import OrderedDict

od = OrderedDict()  

def parse_service_notificaiton(line):
  r = re.compile("(.*SERVICE NOTIFICATION:\s)(.*)")
  notification_group,host_name,service_description,service_state,notification_cmd,plugin_output,junk = r.search(line).group(2).split(";")
#  od.setdefault(host_name, {"Service": service_description, "State": service_state, "StateType": servicestate_type, "Count": 1, "SoftStateChange": 0, "HardStateChange": 0} )
  od[host_name]["Count"] += 1

def parse_current_service_state(line):
  r = re.compile("(.*CURRENT SERVICE STATE:\s)(.*)")
  host_name, service_description, service_state, servicestate_type, service_check_attempt, plugin_output = r.search(line).group(2).split(";")
  od.setdefault(host_name, {"Service": service_description, "State": service_state, "StateType": servicestate_type, "Count": 0, "SoftStateChange": 0, "HardStateChange": 0} )
  od[host_name]["Service"] = service_description
  od[host_name]["State"] = service_state
  od[host_name]["StateType"] = servicestate_type
  od[host_name]["last_state"] = service_state
  od[host_name]["last_statetype"] = servicestate_type

def parse_service_alert(line):
  r = re.compile("(.*SERVICE ALERT:\s)(.*)")
  host_name, service_description, service_state, servicestate_type, service_check_attempt, plugin_output = r.search(line).group(2).split(";")
  od.setdefault(host_name, {"Service": service_description, "State": service_state, "StateType": servicestate_type, "Count": 0, "SoftStateChange": 0, "HardStateChange": 0})
  od[host_name]["Service"] = service_description
  od[host_name]["State"] = service_state
  od[host_name]["StateType"] = servicestate_type
  if "last_state" not in od[host_name].keys():
      od[host_name]['last_state'] = 'OK'
  if od[host_name]["last_state"] != service_state and servicestate_type == 'SOFT':
    od[host_name]["SoftStateChange"] += 1
    od[host_name]["last_state"] = service_state
  if od[host_name]["last_state"] == service_state and service_state != 'OK' and servicestate_type == 'HARD':
    od[host_name]["HardStateChange"] += 1
  if servicestate_type == 'HARD':
    od[host_name]["Count"] += 1

with open('/home/sbathe/work/icinga.log') as f:
    # define all the re's we would match against
   cst = re.compile("(.*CURRENT SERVICE STATE:\s)(.*)")
   sr = re.compile("(.*SERVICE ALERT:\s)(.*)")
   sn = re.compile("(.*SERVICE NOTIFICATION:\s)(.*)")
	
   for line in f:
     if cst.search(line):
       parse_current_service_state(line)
     elif sr.search(line):
       parse_service_alert(line)
     elif sn.search(line):
       parse_service_notificaiton(line)

#print yaml.dump(od, default_flow_style=False, explicit_start=True)

for k,v in od.items():
  print("{}, {}".format(k,v))
