import numpy as np
import cv2
import face_recognition
import os

# upload every photo in the directory in a list
path = 'Data'
imgs = [] # cambialo con un dizionario
names = []
list = os.listdir(path)
for elem in list:
    curimg = cv2.imread(f'{path}/{elem}')
    imgs.append(curimg)
    names.append(os.path.splitext(elem)[0])
del curimg, path, list

# encode every photo of the list
def encode (imgs):
    encode = []
    for elem in imgs:
        elem = cv2.cvtColor(elem, cv2.COLOR_BGR2RGB)
        encode.append(face_recognition.face_encodings(elem)[0])
    return encode

encodeKnownAttendance = encode(imgs)

cap = cv2.VideoCapture(0)

while True:
    # taking the frame from webcam, reshaping it and changing the color from BGR to RGB
    success, frame = cap.read()
    frame = cv2.resize(frame, (0,0), None, 0.25, 0.25)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # locate and encode the faces from the current frame
    locationCurrentFrame = face_recognition.face_locations(frame)
    encodeCurrentFrame = face_recognition.face_encodings(frame, locationCurrentFrame)

    for encodeFace, locationFace in zip(encodeCurrentFrame, locationCurrentFrame):
        # find if there's a face matching from the database
        match = face_recognition.compare_faces(encodeKnownAttendance, encodeFace)
        distance = face_recognition.face_distance(encodeKnownAttendance, encodeFace)
        matchIndex = np.argmin(distance)

        # if the face in the cam is known then save its name taking it from the file name
        if (match[matchIndex]):
            name = names[matchIndex]
        else:
            name = '???'

        # add a rectangle on every face and put the name above it
        y1, x2, y2, x1 = locationFace
        cv2.rectangle(frame, (x1,y1), (x2, y2), (0,0,255), 1)
        cv2.putText(frame, f'{name}', (x1 + 6, y1 - 6), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,255), 1)

    # show the webcam
    cv2.imshow('WebCam', frame)
    cv2.waitKey(1)