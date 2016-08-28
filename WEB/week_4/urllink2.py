# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
tags = soup('span')
total = 0
for tag in tags:
    # Look at the parts of a tag
    contents = int(tag.contents[0])
    total = total + contents
    print 'TAG:',tag
    print 'Contents:',tag.contents[0]
print total