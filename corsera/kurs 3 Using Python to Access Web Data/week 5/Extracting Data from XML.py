import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import xml.etree.cElementTree as ET


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_42.xml'
url = 'http://py4e-data.dr-chuck.net/comments_1235247.xml'
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()
tree = ET.fromstring(data)
results = tree.findall('comments/comment')

total = 0

for item in results:
    total += int(item.find('count').text)

print(total)
