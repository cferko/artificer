import requests
from bs4 import BeautifulSoup
import urllib

urlpath ='http://www.hazmatt.net/gaming/starcraft/zerg/units/'
string = soup = BeautifulSoup(requests.get(urlpath).text)

filelist = [out.split('\');">')[0] for out in str(soup).split(
            "javascript:PlaySound(\'")[1:-1]]

labels = []

for link in soup.findAll('a', href=True)[2:]:
    title = link.contents[0]
    if '<' not in link.contents[0] and "Zerg" not in title:
        if '<' not in str(link.contents[0]):
            labels.append(str(link.contents[0]).lower())

my_path="../audio/"

for index, filename in enumerate(filelist):
    testfile = urllib.URLopener()
    prepend = filename.split('/')[0]
    print 'http://www.hazmatt.net/gaming/starcraft/zerg/units/' + filename
    output_name = (my_path+prepend+"_"+labels[index]+".wav").replace(' ', '')
    testfile.retrieve(urlpath + filename, output_name)