
import urllib.request, re

web = urllib.request
req = web.urlopen('http://www.python.org')
html = req.read()
print(html)

web.close()