#!/usr/bin/env python

import bs4, requests
bulkurl = "https://www.nseindia.com/products/dynaContent/equities/equities/bulkdeals.jsp?symbol=&segmentLink=13&symbolCount=&dateRange=24month&fromDate=&toDate=&dataType=DEALS"
blockurl = 'https://www.nseindia.com/products/dynaContent/equities/equities/blockdeals.jsp?symbol=&segmentLink=12&symbolCount=&dateRange=24month&fromDate=&toDate=&dataType=BLOCK'
#r = requests.get(url)
#data = r.text
#soup = bs4.BeautifulSoup(data,"lxml")
#csvdivdata = soup.find_all(id='csvContentDiv')
#d = csvdivdata[0]
#csvdata = d.contents[0].replace(':','\n')
#csvdata = soup.find_all(id='csvContentDiv')[0].contents[0].replace(':','\n')
#f = open('2yrsbulkdata.csv', 'w')
#f.write(csvdata)

def getcsvdata(url):
    r = requests.get(url)
    data = r.text
    soup = bs4.BeautifulSoup(data,"lxml")
    csvdata = soup.find_all(
        id='csvContentDiv')[0].contents[0].replace(':','\n')
    return csvdata

def writefile(name,data):
    f = open(name, 'w')
    f.write(data)

blockcsv = getcsvdata(blockurl)
bulkcsv = getcsvdata(bulkurl)
writefile('2yrsblock.csv',blockcsv)
writefile('2yrsbulk.csv',bulkcsv)
