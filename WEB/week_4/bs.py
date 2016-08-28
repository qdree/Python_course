import urllib
from BeautifulSoup import *

count = 0

url = raw_input('Enter URL - ')
position = int(raw_input('Position to retrieve - '))
times = int(raw_input('Times to retrieve - '))

names = []

while count < times+1:
    print "retrieving: {0}".format(url)
    html = urllib.urlopen(url)
    soup = BeautifulSoup(html)
    tag = soup('a')
    name = tag[position-1].string
    names.append(name)
    url = tag[position-1]['href']
    count += 1
