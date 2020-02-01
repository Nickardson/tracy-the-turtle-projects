# Pong!
import urllib.request

x = urllib.request.urlopen('http://127.0.0.1:8080/pong/api/login')
html = x.read()
print(html)
