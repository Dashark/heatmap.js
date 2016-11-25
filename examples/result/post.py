# -*- coding: utf-8 -*
import glob,sys,time,json,urllib.request,shutil
import xml.etree.ElementTree as ET
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
url = "https://swifi.cnzz.com/camlog"
body = 'data='+json.dumps(cameras)
bytes = body.encode('utf-8')
res = urllib.request.urlopen(url, bytes)
ret = json.loads(res.read().decode('utf-8'))
if(ret['ret'] == 0) and (ret['msg'] == 'OK'):
  for file in glob.glob('result/*.xml'):
    shutil.move(file, 'result/archived')
else:
  print("upload failed. didn't move files")
 