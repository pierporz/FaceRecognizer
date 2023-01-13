# Face Detection App
This app is a simple program that allows you to select an image and detect the number of faces in it using a pre-trained facial detection model. The image is then resized to 600x400 and displayed on the screen.

## Features
* Select an image using a file dialog
* Detect faces in the selected image using a pre-trained facial detection model
* Draw rectangles around the detected faces
* Show the number of detected faces
* Display the image with the detected faces

## Requirements
This application requires the following Python libraries:
* opencv-python
* pillow
You can install these libraries by running the following command:

` ` ` pip install -r requirements.txt ` ` ` 

## Usage
1. Run the script using main.py
2. Click the "Select Image" button to open the file dialog and select an image
3. The image will be displayed with rectangles around the detected faces and the number of detected faces will be shown
## Limitations
* The script only works with images, other file types will not be accepted
* The script only detects faces, other objects will not be recognized
* The script requires an image with a resolution of at least 900x600
## Note
* The script uses the haarcascade_frontalface_default.xml file for facial detection, which is a pre-trained model. If this file is not present in the same directory as the script, the script will not work.
* The script uses the LANCZOS resampling method to resize the image, which is recommended as the ANTIALIAS method is deprecated and will be removed in Pillow 10 (2023-07-01).