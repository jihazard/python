
import urllib.request, re

web = urllib.request.urlopen('http://www.python.org')
html = web.read()

code = str(html).encode('utf-8').decode('cp949')
web.close()