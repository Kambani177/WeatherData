

import sys
import urllib.request

#asks user for a month
x = input("Enter month: ")

#fetches month depending on user input
url = "https://grader.eecs.jacobs-university.de/courses/350112/python/csv/\
       exp2008" + x + ".csv"
#writing data in a csv file
outfile = 'wdata1.csv'

try:
  u = urllib.request.urlretrieve(url, outfile)
except:
  print("Error fetching URL: ", url)
  sys.exit(1)


