from tkinter import *
from tkinter import ttk
import numpy as np
import cv2

def createCamera():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        cv2.imshow('frame', frame)

        if cv2.waitKey(1) == ord('q'):
            break
    cap.release()

root = Tk()
root.title('Face Recognition')

button_frame = Frame(root, background="green", padx=15, pady=15)
button_frame.pack(fill=BOTH, expand=True)

start_capture_button = Button(button_frame, text="Start capture", font=("Consolas", 15), command=createCamera)
start_capture_button.pack()

end_capture_button = Button(button_frame, text="End capture", font=("Consolas", 15))
end_capture_button.pack()

root.mainloop()