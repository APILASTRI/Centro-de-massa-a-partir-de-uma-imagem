# ROTINA PARA OBTER CENTRO DE MASSA DE UMA OBJETO EM 2D A PARTIR DE UMA FOTO
# ALEXANDRE DE CASTRO MACIEL, DEP. DE FISICA DA UFPI
# MARCO DE 2016
# EXPLICACAO EM http://wp.me/P4JOA-gI

import matplotlib.pyplot as plt
import os
import os.path
import cv2

filename = 'shape.png'
threshold = 200

url = os.path.dirname(os.path.abspath(__file__))
img = cv2.imread(url+'/'+filename, cv2.CV_LOAD_IMAGE_GRAYSCALE)
ret,thresh = cv2.threshold(img,threshold,255,cv2.THRESH_BINARY)
height, width = thresh.shape[:2]

mass = 0
Xcm  = 0.0
Ycm  = 0.0

for i in range(width) :
    for j in range(height) :
        if not thresh[j][i] :
            mass += 1
            Xcm  += i
            Ycm  += j

Xcm = Xcm/mass
Ycm = Ycm/mass

fig = plt.figure()
fig.clear()
plot = fig.add_subplot(111)
plot.imshow(thresh, 'gray')
plot.scatter([Xcm], [Ycm], s=30, c='yellow', edgecolors='red')