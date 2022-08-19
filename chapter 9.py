import cv2
# face detection using cascade method
faceCascade = cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")
img = cv2.imread('Resources/lena.png')
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(imgGray,1.1,4) #scale factors, min neighbours


for (x,y,w,h) in faces: # creating a bounding box
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2) #draw rectangle
    #(img,initial points, corner points, color,thickness)
cv2.imshow("Result",img)
#cv2.imshow("Gray", imgGray)
cv2.waitKey(0)