import json
import urllib.request, urllib.parse, urllib.error
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = "http://py4e-data.dr-chuck.net/comments_1235248.json"
uh = urllib.request.urlopen(url, context = ctx)

data = json.loads(uh.read())
#print(data)

sum = 0

for item in data["comments"]:
    sum += item["count"]

print(sum)