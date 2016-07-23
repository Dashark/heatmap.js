import glob,sys
import xml.etree.ElementTree as ET
print(sys.path[0])
print(glob.glob(sys.path[0]+'/BI/*.xml'))
xmls = [ET.parse(file) for file in glob.glob(sys.path[0]+'/BI/*.xml')]
roots = [xml.getroot() for xml in xmls]
datas = [root[0][3].text.split('.') for root in roots]
[data.pop() for data in datas]
values = [[int(v) for v in data] for data in datas]
sums = [sum(i) for i in zip(*values)]
strsums = [str(sum) for sum in sums]
onestrsums = ' '.join(strsums)

roots[0][0][3].text = onestrsums
xmls[0].write(sys.path[0]+'/BI/output.xml')