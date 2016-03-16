from urllib2 import urlopen

urlpath =urlopen('http://www.hazmatt.net/gaming/starcraft/zerg/units/')
string = urlpath.read().decode('utf-8')

filelist = [out.split('\');">')[0] for out in string.split("javascript:PlaySound(\'")[1:-1]]
print(filelist)

my_path="../audio/"

for filename in filelist:
    print 'http://www.hazmatt.net/gaming/starcraft/zerg/units/' + filename
    remotefile = urlopen('http://www.hazmatt.net/gaming/starcraft/zerg/units/' + filename)
    
    save_name = filename.split("/")[-1]
    localfile = open(my_path+save_name, 'w')
    localfile.write(remotefile.read())
    localfile.close()
    remotefile.close()