import cv2 


cap = cv2.VideoCapture(0)
car_cascade = cv2.CascadeClassifier('cars.xml')

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cars = car_cascade.detectMultiScale(gray, 1.1, 1)
    font = cv2.FONT_HERSHEY_SIMPLEX
    for (x, y, w, h) in cars:   
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.putText(frame, "Car", (x + 6, y - 6), font, 0.5, (0, 0, 255), 1)
    cv2.imshow("Numer Recognition", frame)
    if cv2.waitKey(23) == 13:
        break

cap.release()
cv2.destroyAllWindows()