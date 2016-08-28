import xml.etree.ElementTree as ET
import urllib 

total = 0
names_cnt = 0

url = raw_input("Enter URL: ")

if len(url) < 1: url = "http://python-data.dr-chuck.net/comments_303148.xml"
print "Retrieving: %s"%url

urlhand = urllib.urlopen(url)
data = urlhand.read()

tree = ET.fromstring(data)

print "Characters retrieved: %d"%len(data)

comments = tree.findall("./comments/comment")

for comment in comments:
   total += int(comment.find('count').text)

for n in tree.findall("./comments/comment"):
	name = n.find("name").text
	names_cnt += 1
	#print name

print "Names found: %d"%names_cnt, "\nComments counted: %d"%total