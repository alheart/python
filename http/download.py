import urllib2
response = urllib2.urlopen('http://192.168.1.60')
data = response.read()
print(data)