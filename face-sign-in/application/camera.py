import cv2
import face_recognition

# Load the cascade
face_cascade = cv2.CascadeClassifier("C:\\Users\\Azam\\Desktop\\face-sign-in\\application\\haarcascade_frontalface_default.xml")
# Read the input image
img = cv2.imread("C:\\Users\\Azam\\Desktop\\face-sign-in\\application\\uploads\\1d6cf4524fff1043b210abc9459d4cd6.png")
print(img)
# Convert into grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Detect faces
faces = face_cascade.detectMultiScale(gray, 1.1)
# Draw rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    crop_img = img[y:y+h, x:x+w]
cv2.imshow("cropped", crop_img)
# Display the output
#cv2.imshow('img', img)
cv2.waitKey()