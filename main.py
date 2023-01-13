import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2

# global variable for the image
image = None

# global variable for the text
text = None

def select_image():
    global image
    global text

    # Open a file dialog to select an image
    path = filedialog.askopenfilename()

    # Check if the selected file is an image and if its resolution is lower than 1024x800
    try:
        with Image.open(path) as img:
            if img.size[0] < 900 or img.size[1] < 600:
                label2.configure(text="Error: Image resolution is too low. Please select an image with a resolution of at least 1024x800.")
                return
    except:
        label2.configure(text="Error: Not a valid image file.")
        return

    # Read the selected image
    image = cv2.imread(path)

    # Detect faces in the image using a pre-trained facial detection model
    face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # Draw rectangles around the detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Show the number of detected faces
    text = "There are " + str(len(faces)) + " faces"
    # update the label with the new text
    label2.configure(text=text)

    # Convert the image to a PhotoImage object to display it in tkinter
    image = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    image = image.resize((600,400), Image.LANCZOS)
    image = ImageTk.PhotoImage(image)

    # update the label with the new image
    label.configure(image=image)
    label.image = image


root = tk.Tk()
root.title("Face Detection")
root.geometry("800x600")
root.minsize(width=800, height=600)

# Create a button to open the file dialog
select_button = tk.Button(text="Select Image", command=select_image)
select_button.pack()

# Create a label to display the image
label = tk.Label()
label.pack()

# Create a label to display the text
label2 = tk.Label()
label2.pack()

root.mainloop()
