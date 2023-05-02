import cv2
import face_recognition

# FIXME modificare il nome del file con il proprio
img = cv2.imread("data/giorgia.jpg")
rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_encoding = face_recognition.face_encodings(rgb_img)[0]

vid = cv2.VideoCapture(0)

while not(cv2.waitKey(1) & 0xFF == ord('q')):

    # Capture the video frame
    # by frame
    ret, frame = vid.read()
    # resizing the frame igm for faster comparison
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
    face_locations = face_recognition.face_locations(rgb_small_frame, model='cnn')
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
    for fc in face_encodings:
        result = face_recognition.compare_faces([img_encoding], fc)
        print("Result: ", result)

    # Display the resulting frame
    cv2.imshow('frame', frame)


# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()
