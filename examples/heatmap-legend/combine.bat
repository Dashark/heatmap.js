@echo off
chcp 65001

mkdir C:\Users\huzong\Documents\GitHub\heatmap.js\examples\heatmap-legend\BI
copy C:\Users\huzong\Downloads\两半球热图\captrue1*.xml C:\Users\huzong\Documents\GitHub\heatmap.js\examples\heatmap-legend\BI
C:\Users\huzong\Downloads\python-3.5.2-embed-amd64\python.exe C:\Users\huzong\Documents\GitHub\heatmap.js\examples\heatmap-legend\combine.py
move C:\Users\huzong\Documents\GitHub\heatmap.js\examples\heatmap-legend\BI C:\Users\huzong\Documents\GitHub\heatmap.js\examples\heatmap-legend\captrue1

mkdir C:\Users\huzong\Documents\GitHub\heatmap.js\examples\heatmap-legend\BI
copy C:\Users\huzong\Downloads\两半球热图\captrue2*.xml C:\Users\huzong\Documents\GitHub\heatmap.js\examples\heatmap-legend\BI
C:\Users\huzong\Downloads\python-3.5.2-embed-amd64\python.exe C:\Users\huzong\Documents\GitHub\heatmap.js\examples\heatmap-legend\combine.py
move C:\Users\huzong\Documents\GitHub\heatmap.js\examples\heatmap-legend\BI C:\Users\huzong\Documents\GitHub\heatmap.js\examples\heatmap-legend\captrue2
