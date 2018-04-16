#!/usr/bin/env python
import os, argparse
searchstring = "hostvars[groups['tag_Type_securityServices'][0]]['inventory_hostname']"
replacestring = "squid_proxy_hostname"
parser = argparse.ArgumentParser()
parser.add_argument("-d", action="store", default=os.curdir, dest="directory",
                    help="directory to operate on")
args = parser.parse_args()

for dname, dirs, files in os.walk(args.directory):
    files = [ file for file in files if file.endswith(('.j2','.yml')) ]
    for fname in files:
        if not ".git" in dname:
            fpath = os.path.join(dname,fname)
            print("processing {0}".format(fpath))
            try:
              with open(fpath) as f:
                s = f.read()
            except:
                print('could not process {0}'.format(fpath))
            s = s.replace(searchstring,replacestring)
            with open(fpath,'w') as f:
                f.write(s)
