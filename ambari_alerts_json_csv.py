#!/usr/bin/env python3
import os, sys
import json, csv

def find_file(f,base_dir):
    l = list()
    for root, subdirs, files in os.walk(base_dir):
        if f in files:
            l.append(os.path.join(root,f))
    return l

# The whole block above can also be abbreviated as:
#    l  = [os.path.join(root,f) for root,subdirs,files in os.walk(base) if f in files]

def parse_json(f):
    rows = list()
    j = json.load(open(f))
    s_name = list(j.keys())[0]
    components = list(j[s_name].keys())
    for c in components:
        for item in j[s_name][c]:
            label = item['label'] if 'label' in item.keys() else None
            type = item['source']['type'] if 'type' in item['source'].keys() else None
            desc = item['description'] if 'description' in item.keys() else None
            rows.append([label, type, desc])
    return(s_name,rows)

def write_csv(name, rows):
    with open(name+'.csv', 'w') as csvfile:
        writer = csv.writer(csvfile, dialect=csv.excel)
        writer.writerows(rows)

# main starts here
l = find_file('alerts.json','/Users/sbathe/repos/ambari/ambari-server/src/main/resources/common-services')
for f in l:
    name, rows = parse_json(f)
    write_csv(name, rows)
