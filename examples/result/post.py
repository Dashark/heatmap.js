import glob,sys,time,json,urllib.request
import xml.etree.ElementTree as ET
#print(sys.path[0])
#print(glob.glob('C:\\Users\\huzong\\Documents\\GitHub\\heatmap.js\\examples\\result\\*.xml'))
xmls = [ET.parse(file) for file in glob.glob('result\\*.xml')]
roots = [xml.getroot() for xml in xmls]
cameras = []
userIn = ["1", 1]
userOut = ["1", 0]
for root in roots :
  users = []
  camera = ["0000011111"]
  ctime = time.mktime(time.strptime(root[1].text.strip('\"'), "%Y-%m-%d %H:%M:%S"))
  for i in range(0, int(root[4].text)) :
    users.append(userIn)
  for i in range(0, int(root[5].text)) :
    users.append(userOut)
  camera.append(users)
  camera.append(ctime)
  cameras.append(camera)
print(cameras)
url = "https://swifi.cnzz.com/camlog"
body = 'data='+json.dumps(cameras)
print(body)
bytes = body.encode('utf-8')
print(bytes)
res = urllib.request.urlopen(url, bytes)
print(res.read())
