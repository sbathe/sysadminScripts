#!/usr/bin/env python3
# curl -vv "https://www.screener.in/api/company/TATAMOTORS/consolidated/" > out.json
# from that json, get d['warehouse_set']['id']
# Now, get https://www.screener.in/excel/<id>
# You would need to be logged in to get the excel

#curl -vv --cookie-jar scr-cookies -H "Referer: https://www.screener.in/" https://www.screener.in/login/
#curl --help
#curl -vv --user "user:pass" -H "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:57.0) Gecko/20100101 Firefox/57.0" --cookie scr-cookies -H "Referer: https://www.screener.in/login/" -d '{"csrftoken": "ThkTnzW8amtOjEHSJIOM7RXWCRagWddL"}' -X POST https://www.screener.in/login/
#curl -vv --user -H "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:57.0) Gecko/20100101 Firefox/57.0" --cookie scr-cookies -H "Referer: https://www.screener.in/login/" -d '{"username": "", "password": "", "csrftoken": "ThkTnzW8amtOjEHSJIOM7RXWCRagWddL"}' -X POST https://www.screener.in/login/
#curl -vv -H "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:57.0) Gecko/20100101 Firefox/57.0" --cookie scr-cookies -H "Referer: https://www.screener.in/login/" -d '{"username": "", "password": "", "csrftoken": "ThkTnzW8amtOjEHSJIOM7RXWCRagWddL"}' -X POST https://www.screener.in/login/
#curl -vv --cookie-jar scr-cookies -H "Referer: https://www.screener.in/" https://www.screener.in/login/
#curl -vv -H "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11;rv:57.0) Gecko/20100101 Firefox/57.0" --cookie scr-cookies -H "Referer:https://www.screener.in/login/" -d '{"username": "", "password": "", "csrftoken": "C27zZvbZBLthJVZGVjkDWUY3gH6XMB6c"}' -X POST https://www.screener.in/login/
import json, time,csv
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
now = time.strftime("%Y%m%d%H%M%S",time.localtime())
options = Options()
#options.add_argument("--headless")
#driver = webdriver.Firefox(firefox_options=options)
driver = webdriver.Firefox()
driver.get("https://www.screener.in/login/")
u = driver.find_element_by_id("id_username")
p = driver.find_element_by_id("id_password")
username='dummy@gmail.com'
pa='this_is_dummy'
btn = driver.find_element_by_class_name("button-primary")
u.send_keys(username)
p.send_keys(pa)
#btn.submit()
btn.click()
time.sleep(5)
screenurl = "https://www.screener.in/api/screens/108568/"
#screenurl = "https://www.screener.in/api/screens/108568/?order=asc&page=1&sort=EV+to+OP"
def get_results(url):
    driver.get(url)
    time.sleep(5)
    driver.find_element_by_class_name("tabs-menu-item.rawdata").click()
    k = driver.find_element_by_class_name("data").text
    jdata = json.loads(k)
    return jdata

jdata = get_results(screenurl)
total_results = jdata['page']['count']
results = jdata['page']['results']
print(results)
pages = int(total_results / 50)
print(pages)
# At this point we have json having data for first 50 companies.
# we need toiterate over the pages to get the data data for rest of the pages
# and then merge jdata['page']['results'] into results
for i in range(pages):
    url = screenurl + "?page={0}".format(i+2)
    print(url)
    jdata = get_results(url)
    results.extend(jdata['page']['results'])

jdata['page']['results'] = results
jsonfile = open('screenerout-{0}.json'.format(now),'w')
json.dump(jdata,jsonfile,indent=2)
jsonfile.close()
driver.close()

# now process the data
headers = []
for l in jdata['page']['ratios']:
    headers.append(' '.join(l))
headers.append('EVOP EV/Operating Profit')
headers.insert(0,'BSE/NSE Symbol')
headers.insert(1,'Company Name')
print(headers)
csvfile = open('screenerout-{0}.csv'.format(now),'w')
writer = csv.writer(csvfile)
writer.writerow(headers)
for l in results:
    aqm = (l[6]/l[8])
    l.append(aqm)
    writer.writerow(l)

csvfile.close()


