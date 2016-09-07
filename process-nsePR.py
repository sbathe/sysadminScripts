#!/usr/bin/python
# this gives us a iterable file like object of the file.
# Need to extract :
#   1. All Index data
#   2. All symbol data for equities
# For Index, the third Column (SYMBOL) will be empty, but fourth column (SECURITY) will be populated and so will be the  columns 5-9
# While reading in the data, check for the first column, if it is empty, we can skip the row
#
#
# 1. Test if we have a Index or EQ
# 2. sym = list[2] (or list[3] for Index)
# 3. construct the line to append with required fields in required order (OHLCV,Date in YYYYMMDD)
# 4. Open the file with the name "<sym>.csv" in our path (/storage/sbathe/ascii-data/gt/NSE)
# 5. append the line
# 6. Close the file
# 7. next iteration
import zipfile
przip=zipfile.ZipFile("PR20110507.zip")
przip.open("Pd060511.csv","rU")

for line in l.split("\n"):
  # Pass blank lines
  if line.startswith(' '):
    continue # do nothing with this line
  # We test and find that this is a index,
  # Run index specific imports here
  if line.split(",")[2] == ' ':
    if line.split(",")[3] != ' ':
    #  print "this is a index"
      sym=line.split(",")[3]
      apline=line.split(",")[5]+"\t"+line.split(",")[6]+"\t"+line.split(",")[7]+"\t"+line.split(",")[8]+"\t"+line.split(",")[10]+"\t"+date 
  else:
    print "this is EQ" # We know this is EQ
                       # Run EQ specific imports here

