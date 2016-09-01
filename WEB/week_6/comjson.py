import json
import urllib

total = 0

url = raw_input("Enter URL: ")

if len(url) < 1: url = "http://python-data.dr-chuck.net/comments_42.json"
print "Retrieving: %s"%url

urlhand = urllib.urlopen(url)
data = urlhand.read()


info = json.loads(data)
print 'User count:', len(info["comments"])

n = 0
for el in info["comments"]:
    total += info["comments"][n]["count"]
    n += 1
print "Comments counted: %d"%total

