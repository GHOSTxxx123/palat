import PIL.Image
import dlib
import numpy as np
from PIL import ImageFile
import face_recognition_models
from time import perf_counter



ImageFile.LOAD_TRUNCATED_IMAGES = True

face_detector = dlib.get_frontal_face_detector()

predictor_68_point_model = face_recognition_models.pose_predictor_model_location()
pose_predictor_68_point = dlib.shape_predictor(predictor_68_point_model)

predictor_5_point_model = face_recognition_models.pose_predictor_five_point_model_location()
pose_predictor_5_point = dlib.shape_predictor(predictor_5_point_model)

cnn_face_detection_model = face_recognition_models.cnn_face_detector_model_location()
cnn_face_detector = dlib.cnn_face_detection_model_v1(cnn_face_detection_model)

face_recognition_model = face_recognition_models.face_recognition_model_location()
face_encoder = dlib.face_recognition_model_v1(face_recognition_model)


"""def _rect_to_css(rect):

    return rect.top(), rect.right(), rect.bottom(), rect.left()"""


"""def _css_to_rect(css):

    return dlib.rectangle(css[3], css[0], css[1], css[2])"""


def _trim_css_to_bounds(css, image_shape):

    return max(css[0], 0), min(css[1], image_shape[1]), min(css[2], image_shape[0]), max(css[3], 0)


def face_distance(face_encodings, face_to_compare):

    if len(face_encodings) == 0:
        return np.empty((0))

    return np.linalg.norm(face_encodings - face_to_compare, axis=1)


"""def load_image_file(file):

    im = PIL.Image.open(file)
    im = im.convert("RGB")
    return np.array(im)"""


def _raw_face_locations(img, number_of_times_to_upsample=1, model="hog"):

    if model == "cnn":
        return cnn_face_detector(img, number_of_times_to_upsample)
    else:
        return face_detector(img, number_of_times_to_upsample)


def face_locations(img, number_of_times_to_upsample=1, model="hog"):

    #if model == "cnn":
        #return [_trim_css_to_bounds(_rect_to_css(face.rect), img.shape) for face in _raw_face_locations(img, number_of_times_to_upsample, "cnn")]
        #return [_trim_css_to_bounds((face.rect.top(), face.rect.right(), face.rect.bottom(), face.rect.left()), img.shape) for face in _raw_face_locations(img, number_of_times_to_upsample, "cnn")]
    #else:
        #return [_trim_css_to_bounds(_rect_to_css(face), img.shape) for face in _raw_face_locations(img, number_of_times_to_upsample, model)]
    return [_trim_css_to_bounds((face.top(), face.right(), face.bottom(), face.left()), img.shape) for face in _raw_face_locations(img, number_of_times_to_upsample, model)]


"""def _raw_face_locations_batched(images, number_of_times_to_upsample=1, batch_size=128):

    return cnn_face_detector(images, number_of_times_to_upsample, batch_size=batch_size)"""


def batch_face_locations(images, number_of_times_to_upsample=1, batch_size=128):

    def convert_cnn_detections_to_css(detections):
        face = detections
        #return [_trim_css_to_bounds(_rect_to_css(face.rect), images[0].shape) for face in detections]
        return [_trim_css_to_bounds((face.rect.top(), face.rect.right(), face.rect.bottom(), face.rect.left()), images[0].shape)]

    #raw_detections_batched = _raw_face_locations_batched(images, number_of_times_to_upsample, batch_size)
    raw_detections_batched = cnn_face_detector(images, number_of_times_to_upsample, batch_size=batch_size)

    return list(map(convert_cnn_detections_to_css, raw_detections_batched))
    #return list(map([_trim_css_to_bounds((face.rect.top(), face.rect.right(), face.rect.bottom(), face.rect.left()), images[0].shape) for face in detections], raw_detections_batched))


def _raw_face_landmarks(face_image, face_locations=None, model="large"):
    if face_locations is None:
        face_locations = _raw_face_locations(face_image)
    else:
        face_location = face_locations
        #face_locations = [_css_to_rect(face_location) for face_location in face_locations]
        face_locations = [dlib.rectangle(face_location[3], face_location[0], face_location[1], face_location[2]) for face_location in face_locations]

    pose_predictor = pose_predictor_68_point

    if model == "small":
        pose_predictor = pose_predictor_5_point


    return [pose_predictor(face_image, face_location) for face_location in face_locations]

def face_encodings(face_image, known_face_locations=None, num_jitters=1, model="small"):

    raw_landmarks = _raw_face_landmarks(face_image, known_face_locations, model)
    #return [np.array(face_encoder.compute_face_descriptor(face_image, raw_landmark_set, num_jitters)) for raw_landmark_set in raw_landmarks]
    return [np.array(face_encoder.compute_face_descriptor(face_image, raw_landmark_set, num_jitters)) for raw_landmark_set in raw_landmarks ]


"""def compare_faces(known_face_encodings, face_encoding_to_check, tolerance=0.6):

    return list(face_distance(known_face_encodings, face_encoding_to_check) <= tolerance)"""

start = perf_counter()

im = PIL.Image.open("./img1.jpg")
im = im.convert("RGB")

#image = load_image_file("./img1.jpg")
image = np.array(im)

#print(image)
face_encode1 = face_encodings(image, model="large")[0]
#print(face_encode1)

im1 = PIL.Image.open("./img2.jpg")
im1 = im1.convert("RGB")

#face = load_image_file("./img.png")
face = np.array(im1)

know_face = [face_encode1,]

face_location = face_locations(face)
face_encoding = face_encodings(face, face_location)

face_en = face_encoding[0]
#print(know_face, face_en)
#matches = compare_faces(know_face, face_en)
matches = list(face_distance(know_face, face_en) <= 0.6)

#print(matches)

face_distans = face_distance(know_face, face_en)

best_match_index = np.argmin(face_distans) 

end = perf_counter()

print(matches[best_match_index])
print(end - start)
