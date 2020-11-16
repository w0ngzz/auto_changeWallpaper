import requests,re,json,os,sys
import win32api
import win32con
import win32gui

def setWallpaper(image_path):
    key = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER, "Control Panel\\Desktop", 0, win32con.KEY_SET_VALUE)
    win32api.RegSetValueEx(key, "WallpaperStyle", 0, win32con.REG_SZ, "2")
    win32api.RegSetValueEx(key, "TileWallpaper", 0, win32con.REG_SZ, "0")
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, image_path, 1 + 2)
'''
def setWallPaperBMP(imagePath):
    bmpImage = Image.open(imagePath)
    newPath = imagePath.replace('.jpg', '.bmp')
    bmpImage.save(newPath, "BMP")
    setWallpaper(newPath)
'''
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