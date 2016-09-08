import glob,sys,time,json,urllib2
import xml.etree.ElementTree as ET
print(sys.path[0])
print(glob.glob('C:\\Users\\huzong\\Documents\\GitHub\\heatmap.js\\examples\\result\\*.xml'))
xmls = [ET.parse(file) for file in glob.glob('C:\\Users\\huzong\\Documents\\GitHub\\heatmap.js\\examples\\result\\*.xml')]
roots = [xml.getroot() for xml in xmls]
ins = [root[4].text for root in roots]
print(ins)
outs = [root[5].text for root in roots]
print(outs)
camera = ["0000011111"]
user = ["1",1]
users = [];
users.append(user)
camera.append(users)
camera.append(int(time.time()))
print(json.dumps(camera))
