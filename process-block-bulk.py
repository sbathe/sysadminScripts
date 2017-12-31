#!/usr/bin/python
# Bulk deals
#Curl 'https://www.nseindia.com/products/dynaContent/equities/equities/bulkdeals.jsp?symbol=&segmentLink=13&symbolCount=&dateRange=24month&fromDate=&toDate=&dataType=DEALS' -H 'Cookie: ext_name=jaehkpjddfdgiiefcnhahapilbejohhj' -H 'Accept-Encoding: gzip, deflate, br' -H 'Accept-Language: en-US,en;q=0.9' -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36' -H 'Accept: */*' -H 'Referer: https://www.nseindia.com/products/content/equities/equities/bulk.htm' -H 'X-Requested-With: XMLHttpRequest' -H 'Connection: keep-alive' --compressed ;
# Block Deals
#curl 'https://www.nseindia.com/products/dynaContent/equities/equities/blockdeals.jsp?symbol=&segmentLink=12&symbolCount=&dateRange=24month&fromDate=&toDate=&dataType=BLOCK' -H 'Cookie: ext_name=jaehkpjddfdgiiefcnhahapilbejohhj' -H 'Accept-Encoding: gzip, deflate, br' -H 'Accept-Language: en-US,en;q=0.9' -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36' -H 'Accept: */*' -H 'Referer: https://www.nseindia.com/products/content/equities/equities/bulk.htm' -H 'X-Requested-With: XMLHttpRequest' -H 'Connection: keep-alive' --compressed

#soup = BeautifulSoup(open("test.html"))
#table = soup.select_one("table")
#headers = [th.text.encode("utf-8") for th in table.select("tr th")]
#rows = [[td.text.encode("utf-8") for td in row.find_all("td")] for row in table.select("tr + tr")]
import requests

#bulk = open('2yrsbulk.csv').readlines()
#block = open('2yrsblock.csv').readlines()
def get_csv_content(url):
    r = requests.get(url)
    if r.status_code == 200:
        return r.text.splitlines()

#investors = [ "Ramdev", "Raamdeo", "Jhunhunwala", "Rare Enterprises", "Sajay Bakshi", "ValueQuest", "Nirmal Jain", "Indiainfoline", "India infoline", "Kenneth Andrade", "Damani", "Dharamshi", "ValueQuest", "Brightstar", "Nirmal Bang", "Porinju Veliyath", "Nilesh Shah", "Ekansh Mittal", "Mittal Consulting", "Vijay Kedia", "Daljeet Kohli", "Dolly", "rajiv khanna", "Nalanda", "Indianivesh", "india nivesh" ]

investors = [ "Ramdev", "Raamdeo", "Jhunhunwala", "Rare Enterprises", "Sajay Bakshi", "ValueQuest", "Damani", "Dharamshi", "ValueQuest", "Brightstar", "Veliyath", "Nalanda", "Indianivesh", "india nivesh", "Ekansh", "Katalyst Wealth" ]

bulk = get_csv_content('https://nseindia.com/content/equities/bulk.csv')
block = get_csv_content('https://nseindia.com/content/equities/block.csv')
bulkblock = bulk + block

op = ''
for i in investors:
    for line in bulkblock:
        if i.lower() in line.lower():
            op = op + line

open('flags.csv','a').write(op)
