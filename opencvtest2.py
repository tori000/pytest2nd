import cv2
import numpy as np
import matplotlib.pyplot as plt
 
image_path = "gandam.jpg"
img = cv2.imread(image_path)
 
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.merge((gray, gray, gray), img)
 
kernel = np.ones((4,4),np.uint8)
dilation = cv2.dilate(img,kernel,iterations = 1)
 
diff = cv2.subtract(dilation, img)
cv2.imwrite('diff2.png', diff) 

negaposi = 255 - diff
 
plt.imshow(negaposi)

cv2.imwrite('output2.png', negaposi)