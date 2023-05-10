import numpy
import cv2
import face_recognition

# Taking the files
imgBill = face_recognition.load_image_file('Data/Bill Gates.jpg')
imgTest = face_recognition.load_image_file('Data/Gates Test.jpg')

# finding the location of the face
faceLocation = face_recognition.face_locations(imgBill)[0]
encodeBill = face_recognition.face_encodings(imgBill)[0]

locationTest = face_recognition.face_locations(imgTest)[0]
encodeTest = face_recognition.face_encodings(imgTest)[0]

# finds if both imgs are the same person and the distance between them
similarities = face_recognition.compare_faces([encodeBill], encodeTest)
distance = face_recognition.face_distance([encodeBill], encodeTest)

# drawing the rectangle in the photo
cv2.rectangle(imgBill, (faceLocation[3], faceLocation[0]), (faceLocation[1], faceLocation[2]), (0,0,255), 3)
cv2.rectangle(imgTest, (locationTest[3], locationTest[0]), (locationTest[1], locationTest[2]), (0,0,255), 3)

cv2.putText(imgTest, f'{similarities} |  {round(distance[0], 2)}', (50, 50), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,255), 1)

# showing the imgs and waiting for a key to be pressed to close it
cv2.imshow('Bill', imgBill)
cv2.imshow('Test', imgTest)

cv2.waitKey(0)
