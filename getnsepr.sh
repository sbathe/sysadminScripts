#!/bin/bash
wget -U "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11" http://www.nseindia.com/content/equities/PR.zip -O /home/beginbyt/nsedata/PR$(date +%d%m%y).zip
wget -U "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11" http://www.nseindia.com/content/equities/bulk.csv -O /home/beginbyt/nsedata/bulk-$(date +%d%m%y).csv
wget -U "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11" http://www.nseindia.com/content/equities/block.csv -O /home/beginbyt/nsedata/block-$(date +%d%m%y).csv
