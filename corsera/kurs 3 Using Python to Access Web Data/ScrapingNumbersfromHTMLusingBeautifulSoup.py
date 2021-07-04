from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
if url == '':
    url = 'http://py4e-data.dr-chuck.net/comments_42.html'
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
# print(soup)
total = 0
temp = []
for line in soup:
    temp += re.findall('span\sclass="comments">([0-9]*)', str(line))
    
for element in temp:
    total += int(element)
print(total)
