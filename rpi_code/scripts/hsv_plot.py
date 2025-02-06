import cv2
import matplotlib.pyplot as plt
import numpy as np

# Load the image
img = cv2.imread('Pictures/Mite1.jpg')

# Convert the image to HSV
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Convert HSV back to RGB for display
rgb_img = cv2.cvtColor(hsv_img, cv2.COLOR_HSV2RGB)

# Display the original image and the HSV-converted image
fig, ax = plt.subplots(1, 2, figsize=(10, 5))

ax[0].imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
ax[0].set_title('Original Image')
ax[0].axis('off')

ax[1].imshow(hsv_img)
ax[1].set_title('HSV-Converted Image')
ax[1].axis('off')

plt.show()
