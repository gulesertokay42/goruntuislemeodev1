import cv2
import numpy as np

image = cv2.imread("python/goruntuisleme/odev3/pirinc.png")
goruntu = cv2.resize(image, (300, 300))
cv2.imshow("normal_goruntu",goruntu)

gri_goruntu = cv2.cvtColor(goruntu, cv2.COLOR_BGR2GRAY)
cv2.imshow("gri_goruntu",gri_goruntu)

goster, esiklenmis_goruntu = cv2.threshold(gri_goruntu, 100, 255, cv2.THRESH_BINARY)
cv2.imshow("esiklenmis_goruntu",esiklenmis_goruntu)

kernel = np.ones((4, 4), np.uint8)

erozyon = cv2.erode(esiklenmis_goruntu, kernel, iterations=1)
cv2.imshow("erozyon",erozyon)

adet,goster = cv2.findContours(erozyon.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
cerceve = cv2.cvtColor(erozyon, cv2.COLOR_BGR2RGB)

cv2.drawContours(cerceve, adet, -1, (20, 200, 0), 2)
cv2.imshow("Çerçeveleme", cerceve)

print("Pirinc sayisi: ", len(adet))

cv2.waitKey(0)
cv2.destroyAllWindows()