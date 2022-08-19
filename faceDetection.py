import cv2

faceCascade = cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")
img = cv2.imread("Resources/train.JPG")


scalePerc = 25 #scale percentage
width = int(img.shape[1] * scalePerc / 100)
height = int(img.shape[0] * scalePerc / 100)
dsize = (width,height)
resize = cv2.resize(img,(dsize))

imgGray = cv2.cvtColor(resize,cv2.COLOR_BGR2GRAY)
faces = faceCascade.detectMultiScale(imgGray,1.1,4)  #scale factors, min neighbours

for (x,y,w,h) in faces:
    cv2.rectangle(resize,(x,y),(x+w,y+h),(255,0,0),2)#draw rectangle
    # (img,initial points, corner points, color,thickness)

cv2.imshow("Train Pic",resize)
#cv2.imshow("Gray", imgGray)
cv2.waitKey(0)