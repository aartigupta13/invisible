import cv2
import numpy as np
import time

print("""

Harry :  Hey !! Would you like to try my invisibility cloak ??

         Its awesome !!

         Prepare to get invisible .....................
    """)

# Start webcam
cap = cv2.VideoCapture(0)
time.sleep(3)

background = 0
# Capture background (30 frames for better result)
for i in range(30):
    ret, background = cap.read()

# Flip the background
background = np.flip(background, axis=1)

while cap.isOpened():
    ret, img = cap.read()
    if not ret:
        break

    # Flip image
    img = np.flip(img, axis=1)

    # Convert to HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Apply Gaussian blur (optional, for smoothness)
    value = (35, 35)
    blurred = cv2.GaussianBlur(hsv, value, 0)

    # Define range for black color detection
    lower_black = np.array([0, 0, 0])
    upper_black = np.array([180, 255, 30])
    mask = cv2.inRange(hsv, lower_black, upper_black)

    # Refine the mask
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((5,5), np.uint8))
    mask = cv2.dilate(mask, np.ones((5,5), np.uint8), iterations=1)

    # Replace pixels where mask is true with background
    img[np.where(mask == 255)] = background[np.where(mask == 255)]

    # Show result
    cv2.imshow('Invisibility Cloak (Black)', img)

    k = cv2.waitKey(10)
    if k == 27:  # ESC to exit
        break

cap.release()
cv2.destroyAllWindows()
