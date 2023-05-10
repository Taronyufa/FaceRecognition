import numpy as np
import cv2
import face_recognition
import os
from datetime import datetime

# encode every photo of the list
def encode (imgs):
    encode = []
    for elem in imgs:
        elem = cv2.cvtColor(elem, cv2.COLOR_BGR2RGB)
        encode.append(face_recognition.face_encodings(elem)[0])
    return encode

# mark the attendance in a csv file
def markAttendance (name):

    # taking day and time of input and formatting day
    date = datetime.now()
    time = date.strftime('%H:%M:%S')
    month = date.month if (date.month > 9) else f'0{date.month}'
    day = date.day if (date.day > 9) else f'0{date.day}'
    date = f'{date.year}-{month}-{day}'

    with open('Attendance.csv', 'r+') as f:
        dataList = f.readlines()

        # list of all names in the csv file
        nameList = []
        for line in dataList:
            entry = line.split(',')
            nameList.append(entry[0])

        # if the name is not in the list records it
        if (name not in nameList):
            f.writelines(f'\n{name},{date},{time}')
            f.close()
            return

    with open('Attendance.csv', 'r+') as f:
        dataList = f.readlines()

        # find the most recent date of the attendance of the name
        dummy = []
        for line in dataList:
            entry = line.split(',')
            if name in entry:
                dummy.append(entry[1])
        recentdate = max(dummy)

        # if the name is in the list, but his attendance is relative to another day records it
        if (recentdate != date):
            f.writelines(f'\n{name},{date},{time}')
            f.close()
            return

# upload every photo in the directory in a list
path = 'Data'
imgs = [] # cambiare con un dizionario
names = []
list = os.listdir(path)
for elem in list:
    curimg = cv2.imread(f'{path}/{elem}')
    imgs.append(curimg)
    names.append(os.path.splitext(elem)[0])
del curimg, path, list

encodeKnownAttendance = encode(imgs)

cap = cv2.VideoCapture(0)

while True:
    # taking the frame from webcam, reshaping it and changing the color from BGR to RGB
    success, frame = cap.read()
    frame = cv2.resize(frame, (0,0), None, 0.25, 0.25)

    # locate and encode the faces from the current frame
    locationCurrentFrame = face_recognition.face_locations(frame)
    encodeCurrentFrame = face_recognition.face_encodings(frame, locationCurrentFrame)

    for encodeFace, locationFace in zip(encodeCurrentFrame, locationCurrentFrame):
        # find if there's a face matching from the database
        isMatch = face_recognition.compare_faces(encodeKnownAttendance, encodeFace)
        distance = face_recognition.face_distance(encodeKnownAttendance, encodeFace)
        matchIndex = np.argmin(distance)

        # if the face in the cam is known then save its name taking it from the file name
        if (isMatch[matchIndex]):
            name = names[matchIndex]
            markAttendance(name)
        else:
            name = '???'

        # add a rectangle on every face and put the name above it
        y1, x2, y2, x1 = locationFace
        cv2.rectangle(frame, (x1,y1), (x2, y2), (0,0,255), 1)
        cv2.putText(frame, f'{name}', (x1 + 6, y1 - 6), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,255), 1)

    # show the webcam
    cv2.imshow('WebCam', frame)
    cv2.waitKey(1)
