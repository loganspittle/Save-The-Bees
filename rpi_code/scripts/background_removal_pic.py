import cv2
import numpy as np
import matplotlib.pyplot as plt

# Path to the input video
# path = 'Pictures/frame_360.png'
path = 'Pictures/death_march_frames/frame_45.png'

# Open the video file
frame = cv2.imread(path)

# Convert the frame to HSV
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

# Define the range of green color to mask the background
# lower_green = np.array([35, 40, 40])
# upper_green = np.array([85, 255, 255])
lower_green = np.array([140, 0, 0])
upper_green = np.array([162, 255, 255])

# Create a mask for the green background
mask = cv2.inRange(hsv, lower_green, upper_green)

# Invert the mask to keep only the bees
mask = cv2.bitwise_not(mask)

# Apply the mask to the frame to remove the green background
result = cv2.bitwise_and(frame, frame, mask=mask)


# Convert result to grayscale for blob detection
gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)

# Threshold the image
_, thresh = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY)

# Find contours (alternative to blob detection)
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Draw bounding boxes around detected objects
for contour in contours:
    if cv2.contourArea(contour) > 5000:  # Filter small contours
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(result, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Write the processed result to the output video
# Display the original image and the HSV-converted image
fig, ax = plt.subplots(1, 2, figsize=(10, 5))

ax[0].imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
ax[0].set_title('Original Image')
ax[0].axis('off')

ax[1].imshow(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))
ax[1].set_title('Background Removed')
ax[1].axis('off')

plt.show()

