# _FaceFilter-with-OpenCV_

---

## **_Put on sunglasses for the camera._**

![sunglasses](https://github.com/wlals1/FaceFilter-with-OpenCV/raw/master/sunglasses.png)

## You can inspect the face with sunglasses.

## This project requires Python and OpenCV.

---

# Requirements (Used in this repository):

- ## [Python](https://www.python.org/downloads/) 3.11.5
- ## OpenCV 4.8.1

  ### &ensp; `command: python -m pip install opencv-python`

  ### &ensp; [haarcascade_frontalface_alt.xml](https://github.com/oreillymedia/Learning-OpenCV-3_examples/blob/master/haarcascade_frontalface_alt.xml)

  ### &ensp; [haarcascade_eye_tree_eyeglasses.xml](https://github.com/npinto/opencv/blob/master/data/haarcascades/haarcascade_eye_tree_eyeglasses.xml)

- ## [sunglasses image](https://github.com/wlals1/FaceFilter-with-OpenCV/blob/master/sunglasses.png)

---

# **_How to Work_**

# **_detect_and_draw Function:_**

- ## **_Arguments:_**

  - ### img: Current frame image read from the webcam
  - ### cascade: Haar Cascade classifier for face detection
  - ### nested_cascade: Haar Cascade classifier for eye detection
  - ### scale: Scale for resizing the image
  - ### try_flip: Flag for attempting eye direction
  - ### glasses: Sunglasses image

- ## **_*Functionality:*_**

  ### 1. Convert the image read from the webcam to grayscale and resize it.

  ### 2. Use Haar Cascade to detect faces.

  ### 3. Find eyes around the detected face and calculate the center points of the eyes.

  ### 4. Overlay sunglasses on the face using the center points of both eyes.

  ### 5. Return the overlaid image.

# **_overlay_image Function:_**

- ## **_Arguments:_**
  - ### background: Background image
  - ### foreground: Image to overlay
  - ### location: Location to overlay the image
- ## **_Functionality:_**

  ### 1. Overlay sunglasses on the background image.

  ### 2. The transparent part of the sunglasses does not affect the background image.

  ### 3. Return the overlaid image.

# **_Process Description:_**

## &ensp; 1. Load Haar Cascades:

### &ensp; &ensp; Load Haar Cascade classifiers from the files

## &ensp; 2. Load Sunglasses Image:

### &ensp; &ensp; Load the sunglasses image from the 'sunglasses.png' file.

## &ensp; 3. Start Webcam Capture:

### &ensp; &ensp; Open the webcam using OpenCV and begin reading frames.

## &ensp; 4. Frame Processing:

### &ensp; &ensp; Converts the frame to grayscale and resizes it.

### &ensp; &ensp; Utilizes the Haar Cascade classifier to detect faces in the frame.

### &ensp; &ensp; Locates eyes around the detected face and calculates their center points.

### &ensp; &ensp; Overlays sunglasses on the face using the center points of the eyes.

## &ensp; 5. Handle Keyboard Input

### &ensp; &ensp; If the 'q' key is pressed, the program exits.

---

# **_Command:_**

## `python finalcode.py`

---

# **_Result:_**

![Result](https://github.com/wlals1/FaceFilter-with-OpenCV/raw/master/output.gif)
