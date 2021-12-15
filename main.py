import requests,re,json,os,sys

email = str(os.environ['EMAIL'])
username = str(os.environ['USERNAME'])
cmd1 = r'git config --local user.email "' + email +r'"'
cmd2 = r'git config --local user.name "' + username + r'"'
cmd3 = r'git commit -m "a new pic" -a'

req = requests.get("http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1").json()
urlbase = req['images'][0]['urlbase']
url='http://cn.bing.com/'+urlbase+'_UHD.jpg'
print(url)
img = requests.get(url)#.content
name = re.findall(r'OHR.*$',urlbase)
dir = r'.'+ name[0] +r'.jpg'
if os.path.exists(dir) is False:
    fp=open(dir,"wb")
    fp.write(img.content)
    fp.close()
    print('finished')
    #sys.exit()
else:print('existed')
#sys.exit()
os.system(cmd1)
os.system(cmd2)
os.system(cmd3)
