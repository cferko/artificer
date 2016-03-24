import requests
from bs4 import BeautifulSoup
import urllib

urlpath ='http://www.hazmatt.net/gaming/starcraft/zerg/units/'
string = soup = BeautifulSoup(requests.get(urlpath).text)

filelist = [out.split('\');">')[0] for out in str(soup).split(
            "javascript:PlaySound(\'")[1:-1]]

print(filelist)

my_path="../audio/"

for filename in filelist:
    testfile = urllib.URLopener()
    print 'http://www.hazmatt.net/gaming/starcraft/zerg/units/' + filename
    testfile.retrieve(urlpath + filename, my_path+filename.split('/')[-1])