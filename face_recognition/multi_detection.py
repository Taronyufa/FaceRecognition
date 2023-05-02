import glob
import os

import cv2
import face_recognition
import numpy as np


class SimpleFacesRecognition:

    def __init__(self):
        self.known_people = dict()
        self.frame_resizing = 0.25

    def load_images(self, path):
        images_path = glob.glob(os.path.join(path, "*.*"))
        for img_path in images_path:
            img = cv2.imread(img_path)
            rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            img_encoding = face_recognition.face_encodings(rgb_img)[0]
            # naive extraction of the name of the image
            filename = img_path.split('/')[-1].split('.')[0]
            self.known_people[filename] = img_encoding

    def detect_faces(self, frame):
        small_frame = cv2.resize(frame, (0, 0), fx=self.frame_resizing, fy=self.frame_resizing)
        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_locations = np.array(face_locations)
        face_locations = (face_locations / self.frame_resizing).astype(int)
        found = dict()
        for name, encoding in self.known_people.items():
            result = face_recognition.compare_faces(face_encodings, encoding)
            if True in result:
                match_index = result.index(True)
                found[name] = face_locations[match_index]

        return found


detection_model = SimpleFacesRecognition()
# FIXME modificare il path con il nome della cartella in cui avete le immagini
detection_model.load_images('data/')
vid = cv2.VideoCapture(0)

while not(cv2.waitKey(1) & 0xFF == ord('q')):
    ret, frame = vid.read()
    found_faces = detection_model.detect_faces(frame)
    for name, face_loc in found_faces.items():
        y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]

        cv2.putText(frame, name, (x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)
    cv2.imshow('frame', frame)

# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()
