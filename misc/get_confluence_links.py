#!/usr/bin/env python
import sys, os, json, requests, certifi
user = os.environ['c_user']
password = os.environ['c_pass']
url = os.environ['c_url']
debug = 0
try:
    if debug:
        print('getting {0}{1}'.format(url,'/rest/api/content'))
    r = requests.get(url+'/rest/api/content', auth=(user,password),verify=certifi.where())
    results = r.json()['results']
except Exception as e:
    print("Error {0}".format(e))
    sys.exit(1)
web_links = []
for i in results:
    web_links.append(str(i['_links']['webui']))
f = open('/Users/sbathe/work/confluence/all_confluence_pages.txt','w')
[ f.write(url+r+'\n') for r in web_links ]
f.close()
