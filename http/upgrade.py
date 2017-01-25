import requests

url='http://169.254.1.10/upload/upgradesoftware'

files={'file':('IPS3000.bin', open('D://version/IPS3000_v1.0.1.bin', 'rb'))}

r=requests.post(url, files=files)
print(r.text)
