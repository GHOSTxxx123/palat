from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

import matplotlib.pyplot as plt
import pytesseract 
import cv2 


pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

class Numer_Detect(QThread):
    video = pyqtSignal(QImage)

    def __init__(self):
        super().__init__()
        self.starting = True

    def if_number(self, number):
        numbers = [" 015ADM", "05KZ "]

        if number in numbers:
            print("AAAAAAAAAAAAAA")

    def casced_num(self, image, cascad):
        cars = cascad.detectMultiScale(image, 1.1, 5)

        for (x, y, w, h) in cars:  
            carplat_image = image[y + 5:y + h - 10, x + 5:x + w - 20] 
            return self.car_number_text(carplat_image, 70)

    def car_number_text(self, image, scale_percent):
        width = int(image.shape[1] * scale_percent / 100)
        height = int(image.shape[0] * scale_percent / 100)
        dim = (width, height)
        resize_image = cv2.resize(image, dim, cv2.INTER_AREA)

        number = pytesseract.image_to_string(
                    resize_image,
                    config = '--psm 6 --oem 3 -c tessedit_char_writelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
                 )
        
        print(number.replace(" ", "", 5), len(number.replace(" ", "")))

        self.if_number(number.replace(" ", ""))
        

    def run(self):
        cap = cv2.VideoCapture(0)
        car_cascade = cv2.CascadeClassifier('cars_numbers.xml')

        self.starting = True

        while self.starting:
            ret, frame = cap.read()

            self.casced_num(frame, car_cascade)

            gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

            cars = car_cascade.detectMultiScale(gray, 1.1, 5)


            font = cv2.FONT_HERSHEY_SIMPLEX
            for (x, y, w, h) in cars:   
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(frame, "Car", (x + 6, y - 6), font, 0.5, (0, 255, 0), 1)

            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = frame.shape
            bytes_per_line = ch * w

            image = QImage(frame.data, w, h, bytes_per_line, QImage.Format.Format_RGB888)
            image = image.scaled(600, 400, Qt.AspectRatioMode.KeepAspectRatio)

            self.video.emit(image)

class Main_Window(QWidget):
    def __init__(self):
        super().__init__()
        
        self.thread_video = Numer_Detect()
        self.thread_video.video.connect(self.video_stream)
        self.thread_video.start()

        self.video = QLabel("", self)
        self.video.resize(600, 400)
        
        self.sign = QWidget(self)



    def video_stream(self, image):
        self.video.setPixmap(QPixmap.fromImage(image))

    def closeEvent(self, event):
        reply = QMessageBox.question(
                    self, 
                    "Exit", 
                    "Are you sure to quit?", 
                    QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                    QMessageBox.StandardButton.No
        )

        if reply == QMessageBox.StandardButton.Yes:
            self.thread_video.starting = False
            event.accept()
            #self.thread_video
        else:
             event.ignore()


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    win = Main_Window()
    win.setFixedSize(800, 400)
    win.show()
    app.exec()
