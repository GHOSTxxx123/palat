# Импорт необходимых модулей
from imutils.video import VideoStream
import cv2
import numpy as np
import dlib

# Запуск видео потока
vs = VideoStream(src=0).start()

# Подключение детектора, настроенного на поиск человеческих лиц
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("C:/Users/negma/AppData/Local/Programs/Python/Python38/Lib/face_recognition_models/models/shape_predictor_68_face_landmarks.dat")

while True:
 
    # Получение изображения из видео потока
    frame = vs.read()

    # Конвертирование изображения в черно-белое
    grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Обнаружение лиц и построение прямоугольного контура
    faces = detector(grayFrame)

    # Обход списка всех лиц попавших на изображение
    for face in faces:

        # Выводим количество лиц на изображении
        cv2.putText(frame, "{} face(s) found".format(len(faces)), (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

        # Получение координат вершин прямоугольника и его построение на изображении
        x1 = face.left()
        y1 = face.top()
        x2 = face.right()
        y2 = face.bottom()
        cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 1)
 
        # Получение координат контрольных точек и их построение на изображении
        landmarks = predictor(grayFrame, face)
        for n in range(0, 68):
            x = landmarks.part(n).x
            x45 = landmarks.part(45).x
            x42 = landmarks.part(42).x
            x36 = landmarks.part(36).x
            x39 = landmarks.part(39).x
            y45 = landmarks.part(45).y
            y42 = landmarks.part(42).y
            y36 = landmarks.part(36).y
            y39 = landmarks.part(39).y
            YL = (y45 + y42) / 2
            YR = (y39 + y36) / 2
            XL = (x45 + x42) / 2
            XR = (x39 + x36) / 2
            X0 = (XL + XR) / 2
            Y0 = (YL + YR) / 2
            DX = XR - XL
            DY = YR - YL
            L = (DX ** 2 + DY ** 2)
            sin_AL = DY / L
            cos_AL = DX / L
            X_User_0 = (landmarks.part(27).x - X0) / L
            y = landmarks.part(n).y
            cv2.circle(frame, (x, y), 3, (255, 0, 0), -1)

    cv2.putText(frame, "Press ESC to close frame", (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

    # Вывод преобразованного изображения
    cv2.imshow("Frame", frame)

    # Для выхода из цикла нажать ESC
    key = cv2.waitKey(1)
    if key == 27:
        break