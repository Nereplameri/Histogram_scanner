import cv2
import numpy
import numpy as np
from matplotlib import pyplot as plt


foto = cv2.imread("Neko_dillema.jpg")
cv2.imshow("Art", foto)
cv2.waitKey()

histy = []
for i in range(256):
    ## Boş bir histogram listesi oluşturuyor
    histy += [[0]]
# Alperen AVCI 02210201052
for z in range(len(foto)):
    for y in range(len(foto[0])):
        for x in range(len(foto[0][0])):
            ## 3 boyutlu matristeki pikselleri arayıp histograma atıyor
            index = foto[z][y][x]
            histy[index][0] += 1

#Histogram grafiği
plt.figure(1)
plt.plot(histy)
plt.show()
