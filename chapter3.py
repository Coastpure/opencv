import cv2

img = cv2.imread("Resources/lambo.png")
print(img.shape)

imgResize = cv2.resize(img,(300,200)) #we have reduced the pixels
print(imgResize.shape)

imgCropped = img[0:200,200:500] #cropping the image, height from point 0 to 200, width from point 200 to 500

cv2.imshow("Image",img)
cv2.imshow("Image Resize",imgResize)
cv2.imshow("Image Cropped",imgCropped)

cv2.waitKey(0)