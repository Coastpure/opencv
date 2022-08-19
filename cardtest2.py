import cv2
import numpy as np

img = cv2.imread("Resources/cards2.jpg")

width,height = 250,350
points1 = np.float32([[382,80],[582,69],[421,321],[641,305]])
points2 = np.float32([[0,0],[width,0],[0,height],[width,height]])

transform = cv2.getPerspectiveTransform(points1,points2)
imgOutput = cv2.warpPerspective(img,transform,(width,height))

cv2.imshow("Original image",img)
cv2.imshow("Cropped image",imgOutput)
cv2.waitKey(0)