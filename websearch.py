import urllib.request
import urllib.parse
from urllib.request import Request, urlopen
url = 'https://fortnitetracker.com/profile/pc/Juul1501'
f = urllib.request.urlopen(url)
print(f.read().decode('utf-8'))



