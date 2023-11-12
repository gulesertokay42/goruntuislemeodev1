import cv2
import numpy as np
# foto2 = cv2.imread("./goruntu/kanal.png")#klasörden görüntü okuma
# cv2.imshow("Kırmızı",foto2)
foto = cv2.imread("python/goruntuisleme/hafta1/baboon.png")
cv2.imshow("baboon",foto)
#cv2.waitKey()
B = foto[:,:,0]
G = foto[:,:,1]
R = foto[:,:,2]
cv2.imshow("Mavi",B)
cv2.imshow("Yesil",G)
cv2.imshow("Kirmizi",R)
#cv2.waitKey()
foto_gri=cv2.cvtColor(foto,cv2.COLOR_BGR2GRAY)
cv2.imshow("baboon_gri",foto_gri)

cv2.waitKey()
from matplotlib import pyplot as plt
import matplotlib.image as mpimg
imgGray = 0.2989 * R + 0.5870 * G + 0.1140 * B
plt.imshow(imgGray, cmap='gray')
#plt.show()