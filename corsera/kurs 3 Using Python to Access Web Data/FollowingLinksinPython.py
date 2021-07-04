import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

count = 7
position = 18

url = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html'
url = 'http://py4e-data.dr-chuck.net/known_by_Conal.html'
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
taglist = []
# Retrieve all of the anchor tags
for i in range(count):
    tags = soup('a')
    try:
        print(taglist[position-1])
    except:
        pass
    taglist = []
    print()
    
    for tag in tags:
        taglist.append(tag.get('href', None))
    url = taglist[position-1]
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
print(taglist[position-1])