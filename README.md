🧙 Invisibility Cloak (OpenCV Project)

📌 Overview

This project simulates an invisibility cloak effect (inspired by Harry Potter 🪄) using Python and OpenCV.
It detects a chosen color in the webcam feed (here black color 🖤) and replaces it with the pre-captured background, creating the illusion of invisibility.

🚀 Features

Real-time webcam-based cloak effect.

Background capture for seamless blending.

Color detection using HSV color space.

Morphological operations for noise removal.

Smooth and interactive visualization.

🛠️ Technologies Used

Python 3

OpenCV (cv2)

NumPy

📂 Project Structure

invisible/
│── invisibility_cloak.py   # Main Python script

│── README.md               # Project documentation

⚙️ Setup & Installation

Clone the repository:

git clone https://github.com/aartigupta13/invisible.git

cd invisible


Install required dependencies:

pip install opencv-python numpy


Run the script:

python invisibility_cloak.py

🎥 How it Works

The script captures the background for a few seconds.

Any region in the video feed with the target color (black cloak) is detected.

That region is replaced with the background, making it appear invisible.

📷 Demo

(You can add a GIF or screenshot of the cloak effect here later.)

✨ Future Improvements

Allow users to select custom cloak colors.

Add smoother blending with advanced image processing.

Save output video as a file.
