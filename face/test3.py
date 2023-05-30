import face_recognition
#import test_2 as face_recognition
import cv2
import numpy as np

video_capture = cv2.VideoCapture(0 + cv2.CAP_DSHOW)

image1 = face_recognition.load_image_file("./img1.jpg")
face_encoding1 = face_recognition.face_encodings(image1, model='large')[0]


image2 = face_recognition.load_image_file("./img2.jpg")
face_encoding2 = face_recognition.face_encodings(image2, model='large')[0]

known_face_encodings = [
    face_encoding1,
    face_encoding2
]

count = 0

while True:

    ret, frame = video_capture.read()

    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    try:
        face_encoding = face_encodings[0]
        top, right, bottom, left = face_locations[0]
        #right = face_locations[0][1]
        #bottom = face_locations[0][2]
        #left = face_locations[0][3]
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)
    
        if matches[best_match_index] == True:
        
            cv2.rectangle(frame, (left, top), (right, bottom), (50, 205, 50), 2)

        elif matches[best_match_index] == False:

            cv2.imwrite("frame/%d.jpg" % count, frame)

            count += 1

            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

    except:
        pass
 
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()