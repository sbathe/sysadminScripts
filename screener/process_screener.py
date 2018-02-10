#!/usr/local/bin/python3
import json, csv,time

now = time.strftime("%Y%m%d%H%M%S",time.localtime())
# now process the data
jdata = json.load(open('screenerout-20180210190255.json'))
results = jdata['page']['results']
headers = []
for l in jdata['page']['ratios']:
    headers.append(' '.join(l))
headers.append('EVOP EV/Operating Profit')
headers.insert(0,'BSE/NSE Symbol')
headers.insert(1,'Company Name')
print(headers)
csvfile = open('screenerout.csv'.format(now),'w')
writer = csv.writer(csvfile)
writer.writerow(headers)
for l in results:
    l[0] = str(l[0].split('/')[2])
    try:
      aqm = (l[6]/l[10])
    except:
      print("line does not have aqm {0}".format(l))
    l.append(aqm)
    writer.writerow(l)
csvfile.close()
