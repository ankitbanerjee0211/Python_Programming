import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
print('Retrieving', url)
uh = urllib.request.urlopen(url, context = ctx)

data = uh.read()
print('Retrieved', len(data), 'characters')
tree = ET.fromstring(data)

counts = tree.findall('.//count')
sum = 0
num = 0
for item in counts:
    num = int(item.text)
    sum = sum + num

print('Count:', len(counts))
print('Sum:', sum)
