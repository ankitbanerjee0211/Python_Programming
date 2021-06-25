import json
import urllib.request, urllib.parse, urllib.error
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
print('Retrieving', url)
uh = urllib.request.urlopen(url, context = ctx)

data = uh.read()
print('Retrieved', len(data), 'characters')
info = json.loads(data)
print('Count:', len(info['comments']))
sum = 0
num = 0
for i in info['comments']:
    num = int(i['count'])
    sum = sum + num
print('Sum:', sum)
