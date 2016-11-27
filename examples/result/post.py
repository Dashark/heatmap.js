# -*- coding: utf-8 -*
import glob,sys,time,json,urllib.request,shutil
import xml.etree.ElementTree as ET
counts = range(1,99)
rate = [0.1,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2, \
        0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2, \
        0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2, \
        0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2, \
        0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2, \
        0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2, \
        0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2 ]
xmls = [ET.parse(file) for file in glob.glob('result\\*.xml')]
roots = [xml.getroot() for xml in xmls]
strtime = '';
ctime = '';
inNum = 0;
outNum = 0;
for root in roots :
  strtime = root[1].text;
  ctime = time.mktime(time.strptime(root[1].text.strip('\"'), "%Y-%m-%d %H:%M:%S"))
  num = int(root[4].text);
  inNum += num;

  num = int(root[5].text);
  outNum += num;

logfile = open("log.txt", "a+")
num1 = inNum;
rate1 = 0.0;
if inNum in counts :
  rate1 = rate[counts.index(inNum)];
  num1 = int(round(inNum*(1+rate1)));
logfile.write(strtime + '\n');
logfile.write('in:['+str(inNum) +',' + str(num1) + ',' + str(rate1) + ']\n');
num1 = outNum;
rate1 = 0.0;
if outNum in counts :
  rate1 = rate[counts.index(outNum)];
  num1 = int(round(outNum*(1+rate1)));
logfile.write('out:['+str(outNum) +',' + str(num1) + ',' + str(rate1) + ']\n');
logfile.close();

cameras = []
userIn = ["1", 1]
userOut = ["1", 0]
users = []
camera = ["0000011111"]
for i in range(inNum):
  users.append(userIn);
for i in range(outNum):
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
 