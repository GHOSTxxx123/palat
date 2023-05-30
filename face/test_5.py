import pyfirmata
import time
import datetime
import sys
import face_recognition
import numpy as np
import cv2
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

#global board 
#board = pyfirmata.Arduino("COM5")


class ThreadOpenCV_2(QThread, QWidget):
    matches = ['False']

    changePixmap_2 = pyqtSignal(QImage)

    def __init__(self, source):
        super().__init__()

        self.source = source

        self.running = True
        
    def run(self):
        print('start')

        cap_2 = cv2.VideoCapture(self.source)

        self.running = True

        
        while self.running:
            try:
                ret, frame = cap_2.read()

                if ret:
                    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                h, w, ch = frame.shape
                bytes_per_line = ch * w   # PEP8: `lower_case_names` for variables
                
                image = QImage(frame.data, w, h, bytes_per_line, QImage.Format.Format_RGB888)
                image = image.scaled(640, 480, Qt.KeepAspectRatio)

                self.changePixmap_2.emit(image)

            except:
                pass

            
        cap_2.release()
        print('stop')
        
    def stop(self):
        self.running = False


class ThreadOpenCV(QThread, QPushButton):
    
    changePixmap = pyqtSignal(QImage)

    def __init__(self, source):

        super().__init__()

        self.source = source

        self.running = True
        
    def run(self):
        print('start')

        self.win = MainWindow()

        print(self.source)

        cap = cv2.VideoCapture(self.source)


        image1 = face_recognition.load_image_file("./img1.jpg")
        face_encoding1 = face_recognition.face_encodings(image1, model='large')[0]


        image2 = face_recognition.load_image_file("./img_1.jpg")
        face_encoding2 = face_recognition.face_encodings(image2, model='large')[0]

        known_face_encodings = [
            face_encoding1,
            face_encoding2
        ]

        self.known_face_names = [
            "Негматов Аьзам",
            "Юсупов Мухаммедальсаид"
        ]

        self.running = True
        
        while self.running:
            ret, frame = cap.read()


            face_locations = face_recognition.face_locations(frame)
            face_encodings = face_recognition.face_encodings(frame, face_locations)

            try:
                face_encoding = face_encodings[0]
                top, right, bottom, left = face_locations[0]
                #right = face_locations[0][1]
                #bottom = face_locations[0][2]
                #left = face_locations[0][3]
                self.matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

                face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                self.best_match_index = np.argmin(face_distances)
    
                if self.matches[self.best_match_index] == True:
        
                    cv2.rectangle(frame, (left, top), (right, bottom), (50, 205, 50), 2)
                    self.win.recogniti()
                    #today = datetime.datetime.today()
                    #self.btn_6 = QPushButton(f"{self.known_face_names[self.best_match_index]} \n {today.strftime('%Y-%m-%d %H.%M.%S')}", self.win.wid_3)
                    #self.win.layout_2.addWidget(self.btn_5)

                    today = datetime.datetime.today()
                    try:
                        self.btn_6 = QPushButton(f"{self.known_face_names[self.best_match_index]} \n {today.strftime('%Y-%m-%d %H.%M.%S')}", self.win.wid_3)
                        self.win.layout_1.addWidget(self.btn_6)
                        self.btn_6.setStyleSheet("background-color: white; border-radius: 5px; border: 3px solid blue;")
                        #board.digital[13].write(1)
                        #time.sleep(10)
                        #board.digital[13].write(0)
                    except Exception as ex:
                        print(ex)


                elif self.matches[self.best_match_index] == False:

                    cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            except:
                pass                    

            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            h, w, ch = frame.shape
            bytes_per_line = ch * w   # PEP8: `lower_case_names` for variables
                
            image = QImage(frame.data, w, h, bytes_per_line, QImage.Format.Format_RGB888)
            image = image.scaled(225, 390, Qt.AspectRatioMode.KeepAspectRatio)

            self.changePixmap.emit(image)

            
        #cap.release()
        print('stop')
        
    def stop(self):
        self.running = False


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("AS technology")

        #self.thread = ThreadOpenCV(1)

        self.thread_2 = ThreadOpenCV(0)
        self.thread_2.changePixmap.connect(self.setImage)

        self.wid = QLabel(self)
        self.wid.resize(225, 390)
        self.wid.move(50, 100)
        self.wid.setStyleSheet("background-color: black; border-radius: 5px;")
        #self.wid.hide()

        self.wid_1 = QLabel(self)
        self.wid_1.resize(225, 390)
        self.wid_1.move(320, 100)
        self.wid_1.setStyleSheet("background-color: black; border-radius: 5px;")
        #self.wid_1.hide()

        self.wid_2 = QWidget(self)
        self.wid_2.resize(200, 490)
        self.wid_2.move(595, 5)
        self.wid_2.setStyleSheet("background-color: white; border-radius: 5px;")

        self.wid_3 = QWidget(self)
        self.wid_3.resize(200, 490)
        self.wid_3.move(800, 5)
        self.wid_3.setStyleSheet("background-color: white; border-radius: 5px;")

        self.label_3 = QLabel("Выходили", self.wid_3)
        self.label_3.setFont(QFont("Arial", 15))
        self.label_3.move(60, 10)

        self.label_2 = QLabel("Входили", self.wid_2)
        self.label_2.setFont(QFont("Arial", 15))
        self.label_2.move(70, 10)

#        self.widget = QWidget(self.wid_2)
        self.layout_1 = QVBoxLayout(self.wid_2)
        self.layout_2 = QVBoxLayout(self.wid_3)
#        for index in range(15):
#            self.layout_1.addWidget(QLabel(f"label-{index}", self.wid_2))
#        self.widget.setLayout(self.layout_1)                     
#        self.scroll = QScrollArea()
#        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
#        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
#        self.scroll.setWidgetResizable(True)
#        self.scroll.setWidget(self.widget)

#        self.wid_2.setCentralWidget(self.scroll)                  
        self.label_1 = QLabel("  AS technology\nEntertainment 22", self)
        self.label_1.setFont(QFont("Arial", 10))
        self.label_1.move(255, 20)

        self.ip_cam_1 = QLineEdit(self)
        self.ip_cam_1.setPlaceholderText("Ip camera addres")
        self.ip_cam_1.move(55, 65)

        self.ip_cam_2 = QLineEdit(self)
        self.ip_cam_2.setPlaceholderText("Ip camera addres")
        self.ip_cam_2.move(325, 65)

        self.btn_1 = QPushButton("Вход", self)
        self.btn_1.move(200, 65)
        self.btn_1.clicked.connect(self.click_btn_1)

        self.btn_3 = QPushButton("Выход", self)
        self.btn_3.move(470, 65)
        self.btn_3.clicked.connect(self.click_btn_3)

        self.btn_2 = QPushButton("Stop_1", self)
        self.btn_2.move(200, 65)
        self.btn_2.hide()
        self.btn_2.clicked.connect(self.click_btn_2)

        self.btn_4 = QPushButton("Stop_2", self)
        self.btn_4.move(470, 65)
        self.btn_4.hide()
        self.btn_4.clicked.connect(self.click_btn_4)
        
        today = datetime.datetime.today()

        """if self.thread.run().matches[self.thread.run().best_match_index] == True:
            self.btn_6 = QPushButton(f"{self.thread.run().known_face_names[self.thread.run().best_match_index]} \n {today.strftime('%Y-%m-%d %H.%M.%S')}", self.wid_2)
            self.layout_1.addWidget(self.btn_6)"""

    def click_btn_1(self):
        #self.wid.show()
        self.btn_1.hide()
        #self.btn_3.hide()
        self.btn_2.show()
        #self.thread_2 = ThreadOpenCV(self.ip_cam_1.text())
        self.thread_2 = ThreadOpenCV(0)
        self.thread_2.changePixmap.connect(self.setImage)
        self.thread_2.start()
        #self.thread.start()
        
        #if self.thread_2.matches[self.thread_2.best_match_index] == True:
        #    self.btn_3 = QPushButton(f"{self.thread_2.known_face_names[self.thread_2.best_match_index]}", self.wid_2)
        

    def click_btn_2(self):
        #self.wid.hide()
        #self.wid_1.hide()
        self.btn_1.show()
        #self.btn_3.show()
        self.btn_2.hide()
        #self.btn_4.hide()
        today = datetime.datetime.today()
        try:
            if self.thread_2.matches[self.thread_2.best_match_index] == True:
                self.btn_6 = QPushButton(f"{self.thread_2.known_face_names[self.thread_2.best_match_index]} \n {today.strftime('%Y-%m-%d %H.%M.%S')}", self.wid_3)
                self.layout_1.addWidget(self.btn_6)
                self.btn_6.setStyleSheet("background-color: white; border-radius: 5px; border: 3px solid blue;")
                #board.digital[13].write(1)
                #time.sleep(10)
                #board.digital[13].write(0)
        except Exception as ex:
            print(ex)
        #self.thread.running = False
        self.thread_2.running = False
        #board.digital[13].write(0)
    
    def click_btn_4(self):
        #self.wid.hide()
        #self.wid_1.hide()
        #self.btn_1.show()
        self.btn_3.show()
        #self.btn_2.hide()
        self.btn_4.hide()
        today = datetime.datetime.today()
        try:
            if self.thread.matches[self.thread.best_match_index] == True:
                self.btn_6 = QPushButton(f"{self.thread.known_face_names[self.thread.best_match_index]} \n {today.strftime('%Y-%m-%d %H.%M.%S')}", self.wid_2)
                self.layout_1.addWidget(self.btn_6)
                self.btn_6.setStyleSheet("background-color: white; border-radius: 5px; border: 3px solid blue;")
                #board.digital[13].write(1)
                #time.sleep(10)
                #board.digital[13].write(0)
        except:
            pass
        self.thread_2.running = False
        #self.thread.running = False
    
    def click_btn_3(self):
        #self.wid_1.show()
        #self.btn_1.hide()
        self.btn_3.hide()
        #self.btn_2.hide()
        self.btn_4.show()
        self.thread_2 = ThreadOpenCV(self.ip_cam_1.text())
        self.thread_2.changePixmap.connect(self.setImage)
        #self.thread.start()
        self.thread_2.start()
        #self.thread.running = True


    def setImage(self, image):
        self.wid.setPixmap(QPixmap.fromImage(image))
        #self.wid_1.setPixmap_2(QPixmap.fromImage(image))

    def recogniti(self):
        today = datetime.datetime.today()
        try:
            if self.thread_2.matches[self.thread_2.best_match_index] == True:
                self.btn_6 = QPushButton(f"{self.thread_2.known_face_names[self.thread_2.best_match_index]} \n {today.strftime('%Y-%m-%d %H.%M.%S')}", self.wid_3)
                self.layout_1.addWidget(self.btn_6)
                self.btn_6.setStyleSheet("background-color: white; border-radius: 5px; border: 3px solid blue;")
                #board.digital[13].write(1)
                #time.sleep(10)
                #board.digital[13].write(0)
        except Exception as ex:
            print(ex)


if __name__ == '__main__':  

    app = QApplication(sys.argv)  
    window = MainWindow()  
    window.resize(1005, 500)
    window.show()  
    app.exec()  
