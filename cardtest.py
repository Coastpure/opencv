import  cv2 #warping perspective
import numpy as np

img = cv2.imread("Resources/cards2.jpg")

width,height = 250,350
points1 = np.float32([[103,424],[326,400],[116,789],[405,742]])
points2 = np.float32([[0,0],[width,0],[0,height],[width,height]])

transform = cv2.getPerspectiveTransform(points1,points2)
imgOutput = cv2.warpPerspective(img,transform,(width,height))

cv2.imshow("Image",img)
cv2.imshow("Cropped Image",imgOutput)
cv2.waitKey(0)
