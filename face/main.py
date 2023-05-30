import test_2 as face_recognition
import numpy as np

image = face_recognition.load_image_file("./img1.jpg")
#print(image)
face_encode1 = face_recognition.face_encodings(image, model="large")[0]
#print(face_encode1)

face = face_recognition.load_image_file("./img.png")

know_face = [face_encode1,]

face_location = face_recognition.face_locations(face)
face_encoding = face_recognition.face_encodings(face, face_location)

face_en = face_encoding[0]
#print(know_face, face_en)
matches = face_recognition.compare_faces(know_face, face_en)

print(matches)

face_distans = face_recognition.face_distance(know_face, face_en)

best_match_index = np.argmin(face_distans) 

#print(matches[best_match_index])



