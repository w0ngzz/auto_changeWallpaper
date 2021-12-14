import requests,re,json,os,sys

req = requests.get("http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1").json()
urlbase = req['images'][0]['urlbase']
url='http://cn.bing.com/'+urlbase+'_UHD.jpg'
print(url)
img = requests.get(url)#.content
name = re.findall(r'OHR.*$',urlbase)
dir = r'D:/wallpaper/'+ name[0] +r'.jpg'
if os.path.exists(dir) is False:
    fp=open(dir,"wb")
    fp.write(img.content)
    fp.close()
    setWallpaper(dir)
    print('finished')
    #sys.exit()
else:print('existed')
#sys.exit()
