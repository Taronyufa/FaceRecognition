import tkinter as tk
import numpy as np
import cv2
from PIL import Image, ImageTk
import os

# saves the img in the 'Data' directory
def send():
    path = os.path.join(os.getcwd(), 'Data')
    fileName = f'{entry.get()}.jpg'
    cv2.imwrite(os.path.join(path, fileName), img)
    root.destroy()

def takeCapture():
    # cleans the current window
    for widgets in frame.winfo_children():
        widgets.destroy()

    # takes the capture
    global img
    result, img = cap.read()

    # displays the capture in the window when taken
    if result:
        label_widget = tk.Label(frame)
        label_widget.pack()

        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGBA)
        captured_image = Image.fromarray(img)
        photo_image = ImageTk.PhotoImage(image=captured_image)

        label_widget.photo_image = photo_image
        label_widget.configure(image=photo_image)

    # writes "nome e cognome" above the form
    text = tk.Label(frame, text='Nome e Cognome')
    text.pack()

    # creates the form
    global entry
    entry = tk.Entry(frame)
    entry.pack()

    # creates the submit button
    submit = tk.Button(frame, text='Submit', command=send)
    submit.pack()

# shows camera input and puts them inside the window
def openCamera():

    result, image = cap.read()
    opencv_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGBA)

    captured_image = Image.fromarray(opencv_image)
    photo_image = ImageTk.PhotoImage(image=captured_image)

    label_widget.photo_image = photo_image
    label_widget.configure(image=photo_image)
    label_widget.after(10, openCamera)


if __name__ == '__main__':

    # creates the window
    root = tk.Tk()
    root.geometry("800x620")
    root.title('Face Recognition')
    frame = tk.Frame(root)
    frame.pack()

    # takes the camera input and sizes it appropriately
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 800)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 600)

    # runs openCamera function
    label_widget = tk.Label(frame)
    label_widget.pack()
    openCamera()

    # creates the "take capture" button
    takeCaptureButton = tk.Button(frame, text='Take Capture', command=takeCapture)
    takeCaptureButton.pack()

    frame.mainloop()
